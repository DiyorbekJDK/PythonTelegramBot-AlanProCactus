import telebot
from telebot import types

bot = telebot.TeleBot('5906498689:AAHA3u4NAM6bN_fzeGSqXcWl05xJL2Dx6CI')
print("Bot has started")

youTubeChannel = "https://youtube.com/@user-el5ib2sd6r"
telegramLink = "https://t.me/Alan_pro_kaktus"
telegramChanel = '@Alan_pro_kaktus'
newVideo = "https://youtube.com/shorts/kY4UkPUsPUE?feature=share"
popular_video = "https://youtu.be/dWkLFHCgdQ4"
popular_shorts = "https://youtube.com/shorts/wYA2RCjnUKo?feature=share"
photo = open('D:/Programming/PyCharm/PyCharmProjects/TelegrammBots/Photos/second_photo.jpg', 'rb')
photo_two = open('D:/Programming/PyCharm/PyCharmProjects/TelegrammBots/Photos/new_photo.jpg', 'rb')
photo_three = open('D:/Programming/PyCharm/PyCharmProjects/TelegrammBots/Photos/channel_photo.jpg', 'rb')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Choose the language.\nВыбирите язык.\nTilni tanlang.\nТілді таңдаңыз\n Забонро интихоб кунед\n/english - 🇬🇧English language\n/russian -🇷🇺Русский язык\n/uzbek - 🇺🇿O'zbek tili\n/kazakh - 🇰🇿Қазақ тілі\n/tajik - 🇹🇯тоҷикӣ"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['english'])
def english(message):
    if message.text == '/english':
        mess = f"Hi, <b>{message.from_user.first_name}</b>! I am telegram bot Alan Pro Cactus. I can give you information about the Alan Pro Cactus Channel. Everything you need in the menu\n/menu"
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler(commands=["channels"])
        def podpiska(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Are you subscribed for to the YouTube channel?", url=youTubeChannel))
            markup.add(
                types.InlineKeyboardButton("Are you subscribed for to the Telegram channel?", url=telegramLink))
            button3 = types.InlineKeyboardButton('I subscribed', callback_data="user")
            markup.add(button3)
            bot.send_message(message.chat.id, "Channels:", reply_markup=markup)

        @bot.message_handler(commands=['programmer'])
        def programmer(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("I want to order my own Bot. Free?",
                                                  url="https://t.me/Diyorbekdavronov07072007"))
            bot.send_message(message.chat.id, 'Bots Creator:', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "user":
                try:
                    abcd = False
                    a = bot.get_chat_member(chat_id=telegramChanel, user_id=call.from_user.id)
                    if not a.status == 'left':
                        bot.answer_callback_query(call.id, text="You passed the test", show_alert=True)
                        abcd = True
                    else:
                        bot.answer_callback_query(call.id, text="Well Done!", show_alert=True)
                except:
                    bot.answer_callback_query(call.id, text="Excellent!", show_alert=True)

        @bot.message_handler(commands=["menu"])
        def butons(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            youtube = types.KeyboardButton(
                'YouTube channel')
            telegram = types.KeyboardButton('Telegram channel')
            infa = types.KeyboardButton('Information about Alan Pro Cactus')
            markup.add(youtube, telegram, infa)
            bot.send_message(message.chat.id, "Menu:", reply_markup=markup)

        @bot.message_handler(commands=["new"])
        def butons(message):
            bot.send_message(message.chat.id, "New video:")
            bot.send_message(message.chat.id, newVideo)

        @bot.message_handler()
        def text_from_user(message):
            if message.text == 'YouTube channel':
                g = 'Subscribe to the YouTube channel:'
                bot.send_message(message.chat.id, g)
                bot.send_message(message.chat.id, youTubeChannel)
            elif message.text == 'Telegram channel':
                b = 'Subscribe to the Telegram channel:'
                bot.send_message(message.chat.id, b)
                bot.send_message(message.chat.id, telegramLink)
            elif message.text == 'Information about Alan Pro Cactus':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                decription = types.KeyboardButton('About channel Alan Pro Cactus')
                photo_atom = types.KeyboardButton('Alan Pro cactus Photos')
                video = types.KeyboardButton('Most Viewed Alan Pro Cactus Video')
                shorts = types.KeyboardButton('Most Viewed shorts video of Alan Pro Cactus')
                last_video = types.KeyboardButton('The new video')
                markup.add(decription, photo_atom, video, shorts, last_video)
                bot.send_message(message.chat.id, "Information about Alan Pro Cactus:", reply_markup=markup)
            elif message.text == 'About channel Alan Pro Cactus':
                desc = 'Description of the channel Alan Pro Cactus:'
                desc2 = 'Hi my name is Alan pro cactus! I make funny🤣 mysterious🤔beautiful🤤 and cool videos. Subscribe to me!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
            elif message.text == 'Alan Pro cactus Photos':
                bot.send_photo(message.chat.id, photo=photo)
                bot.send_photo(message.chat.id, photo=photo_two)
                bot.send_photo(message.chat.id, photo=photo_three)
            elif message.text == 'Most Viewed Alan Pro Cactus Video':
                desc = 'There is most viewed Alan Pro Cactus Video(Its Horror👻):'
                mesu = 'You should also watch it, keep up with the trend!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_video)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Most Viewed shorts video of Alan Pro Cactus':
                desc = 'There is most viewed short video of Alan Pro Cactus:'
                mesu = 'You should also watch it, keep up with the trend!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_shorts)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'The new video':
                desc = 'There is newer video:'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, newVideo)
            else:
                bot.send_message(message.chat.id, "Unknown command. /menu")

    else:
        mess = f"Choose the language.\nВыбирите язык.\nTilni tanlang.\nТілді таңдаңыз\n Забонро интихоб кунед\n/english - 🇬🇧English language\n/russian -🇷🇺Русский язык\n/uzbek - 🇺🇿O'zbek tili\n/kazakh - 🇰🇿Қазақ тілі\n/tajik - 🇹🇯тоҷикӣ"
        bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['russian'])
def russian(message):
    if message.text == '/russian':
        mess = f"Привет, <b>{message.from_user.first_name}</b>! Я телеграм бот Алана Про кактуса. Я могу дать тебе информацию об Канале Алан Про кактус. Все что нужно в меню\n/menu "
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler(commands=["channels"])
        def podpiska(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Ты подписан на YouTube канал?", url=youTubeChannel))
            markup.add(
                types.InlineKeyboardButton("Ты подписан на телеграм канал?", url=telegramLink))
            button3 = types.InlineKeyboardButton('Я подписался', callback_data="user")
            markup.add(button3)
            bot.send_message(message.chat.id, "Каналы:", reply_markup=markup)

        @bot.message_handler(commands=['programmer'])
        def programmer(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Хочу заказать своего бота. Платно?",
                                                  url="https://t.me/Diyorbekdavronov07072007"))
            bot.send_message(message.chat.id, 'Создатель бота:', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "user":
                try:
                    abcd = False
                    a = bot.get_chat_member(chat_id=telegramChanel, user_id=call.from_user.id)
                    if not a.status == 'left':
                        bot.answer_callback_query(call.id, text="Ты прошёл проверку", show_alert=True)
                        abcd = True
                    else:
                        bot.answer_callback_query(call.id, text="Отлично!", show_alert=True)
                except:
                    bot.answer_callback_query(call.id, text="Молодец!", show_alert=True)

        @bot.message_handler(commands=["menu"])
        def butons(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            youtube = types.KeyboardButton(
                'YouTube канал')
            telegram = types.KeyboardButton('Телеграмм канал')
            infa = types.KeyboardButton('Информация об Алане Про Кактусе')
            markup.add(youtube, telegram, infa)
            bot.send_message(message.chat.id, "Меню:", reply_markup=markup)

        @bot.message_handler(commands=["new"])
        def butons(message):
            bot.send_message(message.chat.id, "Новое видео:")
            bot.send_message(message.chat.id, newVideo)

        @bot.message_handler()
        def text_from_user(message):
            if message.text == 'YouTube канал':
                g = 'Подпишись на YouTube канал:'
                bot.send_message(message.chat.id, g)
                bot.send_message(message.chat.id, youTubeChannel)
            elif message.text == 'Телеграмм канал':
                b = 'Подпишись на Телеграмм канал:'
                bot.send_message(message.chat.id, b)
                bot.send_message(message.chat.id, telegramLink)
            elif message.text == 'Информация об Алане Про Кактусе':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                decription = types.KeyboardButton('О канале Алан Про Кактус')
                photo_atom = types.KeyboardButton('Фото Алана Про Кактуса')
                video = types.KeyboardButton('Самое популярное видео Алана Про Кактуса')
                shorts = types.KeyboardButton('Самое популярный shorts Алана Про Кактуса')
                last_video = types.KeyboardButton('Новое видео Алана Про Кактуса')
                markup.add(decription, photo_atom, video, shorts, last_video)
                bot.send_message(message.chat.id, "Информация об Алане Про Кактусе:", reply_markup=markup)
            elif message.text == 'О канале Алан Про Кактус':
                desc = 'Описание канала Алан Про Кактус:'
                desc2 = 'Привет меня Зовут Алан про кактус! Я снимаю ролики смешные🤣 загадачные🤔 красивые🤤 и крутые Подпишсь на меня!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
            elif message.text == 'Фото Алана Про Кактуса':
                bot.send_photo(message.chat.id, photo=photo)
                bot.send_photo(message.chat.id, photo=photo_two)
                bot.send_photo(message.chat.id, photo=photo_three)
            elif message.text == 'Самое популярное видео Алана Про Кактуса':
                desc = 'Вот его самое популярное видео(Оно Страшное👻):'
                mesu = 'Ты тоже обязательно посмотри его,не отставай от тренда!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_video)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Самое популярный shorts Алана Про Кактуса':
                desc = 'Вот его самый популярный shorts:'
                mesu = 'Ты тоже обязательно посмотри его,не отставай от тренда!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_shorts)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Новое видео Алана Про Кактуса':
                desc = 'Вот новое видео:'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, newVideo)
            else:
                bot.send_message(message.chat.id, "Неправильная команда! /menu")

    else:
        mess = f"Choose the language.\nВыбирите язык.\nTilni tanlang.\nТілді таңдаңыз\n Забонро интихоб кунед\n/english - 🇬🇧English language\n/russian -🇷🇺Русский язык\n/uzbek - 🇺🇿O'zbek tili\n/kazakh - 🇰🇿Қазақ тілі\n/tajik - 🇹🇯тоҷикӣ"
        bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['uzbek'])
def uzbek(message):
    if message.text == '/uzbek':
        mess = f"Salom, <b>{message.from_user.first_name}</b>! Men Alan Pro kaktus telegram botiman. Men sizga Alan Pro Cactus kanali haqida ma'lumot bera olaman. Menyuda sizga kerak bo'lgan hamma narsa\n/menu"
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler(commands=["channels"])
        def podpiska(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("YouTube kanaliga obuna bo'ldingizmi?", url=youTubeChannel))
            markup.add(
                types.InlineKeyboardButton("Siz telegram kanaliga obuna bo'ldingizmi?", url=telegramLink))
            button3 = types.InlineKeyboardButton("Obuna bo'ldim'", callback_data="user")
            markup.add(button3)
            bot.send_message(message.chat.id, "Kanallar:", reply_markup=markup)

        @bot.message_handler(commands=['programmer'])
        def programmer(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Men bot buyurtma kilmoqchiman. Bekarga?",
                                                  url="https://t.me/Diyorbekdavronov07072007"))
            bot.send_message(message.chat.id, 'Bot yaratuvchisi:', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "user":
                try:
                    abcd = False
                    a = bot.get_chat_member(chat_id=telegramChanel, user_id=call.from_user.id)
                    if not a.status == 'left':
                        bot.answer_callback_query(call.id, text="Siz sinovdan o'tdingiz", show_alert=True)
                        abcd = True
                    else:
                        bot.answer_callback_query(call.id, text="Ajoyib!", show_alert=True)
                except:
                    bot.answer_callback_query(call.id, text="Barakalla!", show_alert=True)

        @bot.message_handler(commands=["menu"])
        def butons(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            youtube = types.KeyboardButton(
                'YouTube kanali')
            telegram = types.KeyboardButton('Telegram kanali')
            infa = types.KeyboardButton("Alan Pro Cactus haqida ma'lumot")
            markup.add(youtube, telegram, infa)
            bot.send_message(message.chat.id, "Menu:", reply_markup=markup)

        @bot.message_handler(commands=["new"])
        def butons(message):
            bot.send_message(message.chat.id, "Yangi video:")
            bot.send_message(message.chat.id, newVideo)

        @bot.message_handler()
        def text_from_user(message):
            if message.text == 'YouTube kanali':
                g = "YouTube kanaliga obuna bo'ling:"
                bot.send_message(message.chat.id, g)
                bot.send_message(message.chat.id, youTubeChannel)
            elif message.text == 'Telegram kanali':
                b = "Telegram kanaliga obuna bo'ling:"
                bot.send_message(message.chat.id, b)
                bot.send_message(message.chat.id, telegramLink)
            elif message.text == "Alan Pro Cactus haqida ma'lumot":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                decription = types.KeyboardButton('Alan Pro Cactus kanali haqida')
                photo_atom = types.KeyboardButton('Alan Pro Cactus Rasmi')
                video = types.KeyboardButton("Eng ko'p ko'rilgan Alan Pro kaktus videosi")
                shorts = types.KeyboardButton('Alan Pro Cactusning eng mashhur short videosi')
                last_video = types.KeyboardButton('Alan Pro Cactus tomonidan yangi video')
                markup.add(decription, photo_atom, video, shorts, last_video)
                bot.send_message(message.chat.id, "Alan Pro Cactus haqida ma'lumot:", reply_markup=markup)
            elif message.text == 'Alan Pro Cactus kanali haqida':
                desc = 'Alan Pro Cactus kanalining tavsifi:'
                desc2 = "Salom mening ismim Alan pro kaktus! Men kulgili🤣 sirli🤔chiroyli🤤 va zo'r videolar tayyorlayman.Menga obuna bo'ling!"
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
            elif message.text == 'Alan Pro Cactus Rasmi':
                bot.send_photo(message.chat.id, photo=photo)
                bot.send_photo(message.chat.id, photo=photo_two)
                bot.send_photo(message.chat.id, photo=photo_three)
            elif message.text == "Eng ko'p ko'rilgan Alan Pro kaktus videosi":
                desc = "Mana uning eng mashhur videosi (It's Scary👻):"
                mesu = "Buni ham tekshirib ko'ring, trendni kuzatib boring!"
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_video)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Alan Pro Cactusning eng mashhur short videosi':
                desc = "Mana uning eng mashhur short videosi"
                mesu = "Buni ham tekshirib ko'ring, trendni kuzatib boring!"
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_shorts)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Alan Pro Cactus tomonidan yangi video':
                desc = 'Mana Yangi video:'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, newVideo)
            else:
                bot.send_message(message.chat.id, "Hato! /menu")
    else:
        mess = f"Choose the language.\nВыбирите язык.\nTilni tanlang.\nТілді таңдаңыз\n Забонро интихоб кунед\n/english - 🇬🇧English language\n/russian -🇷🇺Русский язык\n/uzbek - 🇺🇿O'zbek tili\n/kazakh - 🇰🇿Қазақ тілі\n/tajik - 🇹🇯тоҷикӣ"
        bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['kazakh'])
def kazakh(message):
    if message.text == '/kazakh':
        mess = f"Эй, <b>{message.from_user.first_name}</b>! Мен Alan Pro кактусы телеграмма ботымын. Мен сізге Alan Pro Cactus арнасы туралы ақпарат бере аламын. Мәзірде қажет нәрсенің бәрі\n/menu"
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler(commands=["channels"])
        def podpiska(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Сіз YouTube арнасына жазылғансыз ба?", url=youTubeChannel))
            markup.add(
                types.InlineKeyboardButton("Сіз Telegram каналына жазылдыңыз ба?", url=telegramLink))
            button3 = types.InlineKeyboardButton('жазылдым', callback_data="user")
            markup.add(button3)
            bot.send_message(message.chat.id, "Арналар:", reply_markup=markup)

        @bot.message_handler(commands=['programmer'])
        def programmer(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Мен ботыма тапсырыс бергім келеді. Ақылы?",
                                                  url="https://t.me/Diyorbekdavronov07072007"))
            bot.send_message(message.chat.id, 'Бот жасаушы:', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "user":
                try:
                    abcd = False
                    a = bot.get_chat_member(chat_id=telegramChanel, user_id=call.from_user.id)
                    if not a.status == 'left':
                        bot.answer_callback_query(call.id, text="Сіз сынақтан өттіңіз", show_alert=True)
                        abcd = True
                    else:
                        bot.answer_callback_query(call.id, text="Өте жақсы!", show_alert=True)
                except:
                    bot.answer_callback_query(call.id, text="Жарайсың!", show_alert=True)

        @bot.message_handler(commands=["menu"])
        def butons(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            youtube = types.KeyboardButton(
                'YouTube арнасы')
            telegram = types.KeyboardButton('Telegram арнасы')
            infa = types.KeyboardButton('Alan Pro Cactus туралы ақпарат')
            markup.add(youtube, telegram, infa)
            bot.send_message(message.chat.id, "Мәзір:", reply_markup=markup)

        @bot.message_handler(commands=["new"])
        def butons(message):
            bot.send_message(message.chat.id, "Жаңа бейне:")
            bot.send_message(message.chat.id, newVideo)

        @bot.message_handler()
        def text_from_user(message):
            if message.text == 'YouTube арнасы':
                g = 'YouTube арнасына жазылыңыз:'
                bot.send_message(message.chat.id, g)
                bot.send_message(message.chat.id, youTubeChannel)
            elif message.text == 'Telegram арнасы':
                b = 'Telegram арнасына жазылыңыз:'
                bot.send_message(message.chat.id, b)
                bot.send_message(message.chat.id, telegramLink)
            elif message.text == 'Alan Pro Cactus туралы ақпарат':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                decription = types.KeyboardButton('Alan Pro Cactus арнасы туралы')
                photo_atom = types.KeyboardButton('Сурет Alan Pro Cactus')
                video = types.KeyboardButton('Ең көп қаралған Alan Pro Cactus бейнесі')
                shorts = types.KeyboardButton('Alan Pro Cactus Ең танымал shorts бейне')
                last_video = types.KeyboardButton('Alan Pro Cactus ұсынған жаңа бейне')
                markup.add(decription, photo_atom, video, shorts, last_video)
                bot.send_message(message.chat.id, "Alan Pro Cactus туралы ақпарат:", reply_markup=markup)
            elif message.text == 'Alan Pro Cactus арнасы туралы':
                desc = 'Alan Pro Cactus арнасының сипаттамасы:'
                desc2 = 'Сәлем, менің атым Алан про кактусы! Мен күлкілі🤣 жұмбақ🤔әдемі🤤 және керемет бейнелер жасаймын Маған жазылыңыз!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
            elif message.text == 'Сурет Alan Pro Cactus':
                bot.send_photo(message.chat.id, photo=photo)
                bot.send_photo(message.chat.id, photo=photo_two)
                bot.send_photo(message.chat.id, photo=photo_three)
            elif message.text == 'Ең көп қаралған Alan Pro Cactus бейнесі':
                desc = 'Міне, оның ең танымал видеосы (Бұл қорқынышты👻):'
                mesu = 'Оны да көру керек, трендтен қалмау керек!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_video)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Alan Pro Cactus Ең танымал shorts бейне':
                desc = 'Міне, оның ең танымал shorts бейнесі:'
                mesu = 'Оны да көру керек, трендтен қалмау керек!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_shorts)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Alan Pro Cactus ұсынған жаңа бейне':
                desc = 'Міне, жаңа бейне:'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, newVideo)
            else:
                bot.send_message(message.chat.id, "Белгісіз команда")
    else:
        mess = f"Choose the language.\nВыбирите язык.\nTilni tanlang.\nТілді таңдаңыз\n Забонро интихоб кунед\n/english - 🇬🇧English language\n/russian -🇷🇺Русский язык\n/uzbek - 🇺🇿O'zbek tili\n/kazakh - 🇰🇿Қазақ тілі\n/tajik - 🇹🇯тоҷикӣ"
        bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['tajik'])
def tandjik(message):
    if message.text == '/tajik':
        mess = f"Эй, <b>{message.from_user.first_name}</b>! Ман боти телеграмм Alan Pro кактус ҳастам. Ман метавонам ба шумо дар бораи канали Alan Pro Cactus маълумот диҳам. Ҳама чизест, ки ба шумо дар меню\n/menu лозим аст"
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler(commands=["channels"])
        def podpiska(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Шумо ба канали YouTube обуна шудаед?", url=youTubeChannel))
            markup.add(
                types.InlineKeyboardButton("Шумо ба канали телеграм обуна шудаед?", url=telegramLink))
            button3 = types.InlineKeyboardButton('Я подписался', callback_data="user")
            markup.add(button3)
            bot.send_message(message.chat.id, "Каналҳо:", reply_markup=markup)

        @bot.message_handler(commands=['programmer'])
        def programmer(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Ман мехоҳам боти худро фармоиш диҳам. Оё он пардохта мешавад?",
                                                  url="https://t.me/Diyorbekdavronov07072007"))
            bot.send_message(message.chat.id, 'Эҷоди бот:', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "user":
                try:
                    abcd = False
                    a = bot.get_chat_member(chat_id=telegramChanel, user_id=call.from_user.id)
                    if not a.status == 'left':
                        bot.answer_callback_query(call.id, text="Шумо аз имтиҳон гузаштед", show_alert=True)
                        abcd = True
                    else:
                        bot.answer_callback_query(call.id, text="Аъло!", show_alert=True)
                except:
                    bot.answer_callback_query(call.id, text="Офарин!", show_alert=True)

        @bot.message_handler(commands=["menu"])
        def butons(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            youtube = types.KeyboardButton(
                'Канали YouTube')
            telegram = types.KeyboardButton('Телеграм канали')
            infa = types.KeyboardButton('Маълумот дар бораи Alan Pro Cactus')
            markup.add(youtube, telegram, infa)
            bot.send_message(message.chat.id, "Меню:", reply_markup=markup)

        @bot.message_handler(commands=["new"])
        def butons(message):
            bot.send_message(message.chat.id, "Новое видео:")
            bot.send_message(message.chat.id, newVideo)

        @bot.message_handler()
        def text_from_user(message):
            if message.text == 'Канали YouTube':
                g = 'Ба канали YouTube обуна шавед:'
                bot.send_message(message.chat.id, g)
                bot.send_message(message.chat.id, youTubeChannel)
            elif message.text == 'Телеграм канали':
                b = 'Ба канали Telegram обуна шавед:'
                bot.send_message(message.chat.id, b)
                bot.send_message(message.chat.id, telegramLink)
            elif message.text == 'Маълумот дар бораи Alan Pro Cactus':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                decription = types.KeyboardButton('Дар бораи канали Alan Pro Cactus')
                photo_atom = types.KeyboardButton('Сурати Alan Pro Cactus')
                video = types.KeyboardButton('Видеои аз ҳама бештар дидашуда Alan Pro Cactus')
                shorts = types.KeyboardButton('Шортҳои машҳуртарини Alan Pro Cactus')
                last_video = types.KeyboardButton('Видеои нав аз ҷониби Alan Pro Cactus')
                markup.add(decription, photo_atom, video, shorts, last_video)
                bot.send_message(message.chat.id, "Маълумот дар бораи Alan Pro Cactus:", reply_markup=markup)
            elif message.text == 'Дар бораи канали Alan Pro Cactus':
                desc = 'Тавсифи канали Alan Pro Cactus:'
                desc2 = 'Салом номи ман Алан про кактус аст! Ман видеоҳои хандовар🤣 пурасрор🤔 зебо🤤 ​​ва олӣ месозам Ман видеохои хандаовар🤣 пурасрор🤔зебо🤤 ​​ва олича месозам Ба ман обуна шавед!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
            elif message.text == 'Сурати Alan Pro Cactus':
                bot.send_photo(message.chat.id, photo=photo)
                bot.send_photo(message.chat.id, photo=photo_two)
                bot.send_photo(message.chat.id, photo=photo_three)
            elif message.text == 'Видеои аз ҳама бештар дидашуда Alan Pro Cactus':
                desc = 'Ин аст видеои машҳуртарини ӯ (Ин даҳшатнок аст👻):'
                mesu = 'Шумо инчунин бояд онро тамошо кунед, бо тамоюл нигоҳ доред!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_video)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Шортҳои машҳуртарини Alan Pro Cactus':
                desc = 'Дар ин ҷо шортҳои машҳуртарини ӯ ҳастанд:'
                mesu = 'Шумо инчунин бояд онро тамошо кунед, бо тамоюл нигоҳ доред!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, popular_shorts)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Видеои нав аз ҷониби Alan Pro Cactus':
                desc = 'Ана видеои нав:'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, newVideo)
            else:
                bot.send_message(message.chat.id, "Дастаи номаълум")

    else:
        mess = f"Choose the language.\nВыбирите язык.\nTilni tanlang.\nТілді таңдаңыз\n Забонро интихоб кунед\n/english - 🇬🇧English language\n/russian -🇷🇺Русский язык\n/uzbek - 🇺🇿O'zbek tili\n/kazakh - 🇰🇿Қазақ тілі\n/tajik - 🇹🇯тоҷикӣ"
        bot.send_message(message.chat.id, mess)


bot.polling(none_stop=True)
