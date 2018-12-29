"""
DZshnik...
"""
import telebot
import os

# environment variables
bot = os.getenv("TOKEN")
pas_1 = os.getenv("PASSWORD")
pas_2 = os.getenv("PASSWORD2")
pas_3 = os.getenv("PASSWORD3")
token = telebot.TeleBot(bot)
# action send\get bool variables
get_1 = False
get_2 = False
send_1 = False
send_2 = False
get_text_1 = False
get_text_2 = False
news_get = False
news_send = False
photo_get = False
str_add = ""
# command list
string_help = """
start - начать взаимодействие  
Авторы - обратная связь 
Список дз - домашнее задание
Всё дз - всё домашнее задание 
Расписание - расписание 
Команды - список команд
Дежурство - дежурство
Рейтинг - рейтинг
Новости - новости
Назад - вернуться обратно
"""
# token.send_message(402702337,"test")
# upd = token.get_updates()
# print(upd)
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

print(token.get_me())


# log Heroku messaging
def log(message, answer):
    from datetime import datetime
    print("Log-message: ", message, "\nLog-datetime: ", datetime.now, "\nLog-user: ", answer)


# menu creator
def menu(message, send):
    id = message.chat.id
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/Авторы", "/Команды")
    user_markup.row("/Список_дз", "/Всё_дз")
    user_markup.row("/Дежурство", "/Рейтинг")
    user_markup.row("/Расписание", "/Новости")
    token.send_message(id, str(send), reply_markup=user_markup)


# start function
@token.message_handler(commands=["start"])
def handle_text(message):
    global string_help
    id = message.chat.id
    token.send_chat_action(id, "typing")
    menu(message, "Добро пожаловать!")
    token.send_message(id, string_help)


# authors command
@token.message_handler(commands=["Авторы"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, """
Бот был создан учениками ЛИТа 8-В класса Яицким Тарасом, Антоном Мордаком, Хорсуном Дмитрием.
Вопросы? 
taras2005dn@gmail.com
frieddimka@gmail.com
antongimnasium@gmail.com
""")


# commands info
@token.message_handler(commands=["Команды"])
def handle_text(message):
    global string_help
    id = message.chat.id
    token.send_message(id,string_help)

# list of homework
@token.message_handler(commands=["Список_дз"])
def handle_text(message):
    id = message.chat.id
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("ukr.lit", "for.lit")
    user_markup.row("urk.m", "rus.m", "en.m")
    user_markup.row("math", "physics", "informatics")
    user_markup.row("chemistry", "geography", "history")
    user_markup.row("art", "bio", "/Назад")
    token.send_message(id, "Список предметов", reply_markup=user_markup)

# all homework
@token.message_handler(commands=["Всё_дз"])
def handle_text(message):
    global get_1, get_2, news_get
    id = message.chat.id
    token.send_chat_action(id, "typing")
    file_1 = open("week1.txt", "r+")
    file_2 = open("week2.txt", "r+")
    str_default = "|!=--------\---*---#----@--{0} группа--@---#---*---/--------=!|"
    if get_1 is False and get_2 is False and news_get is False:
        token.send_message(id, str_default.format(1))
        for str1 in file_1:
            token.send_message(id, str1)
        token.send_message(id, str_default.format(2))
        for str2 in file_2:
            token.send_message(id, str2)
    file_1.close()
    file_2.close()


# subject list
@token.message_handler(commands=["Расписание"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, 'upload_photo')
    token.send_message(id, """
    Расписание:\n""")
    token.send_photo(chat_id=id, photo=open('8v.png', 'rb'))


# lyceum news
@token.message_handler(commands=["Новости"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, 'upload_photo')
    file_path = "news"
    token.send_message(id, """
    Новости:\n """)
    if os.path.exists(file_path + ".jpg"):
        token.send_photo(chat_id=id, photo=open(file_path + ".jpg", 'rb'))
    if os.path.exists("news.txt"):
        file = open("news.txt", "r")
        for s in file:
            token.send_message(id, s)
        file.close()
    else:
        token.send_message(id, "Новостей нет!")


# rating
@token.message_handler(commands=["Рейтинг"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, 'upload_photo')
    token.send_message(id, "Рейтинг:\n")
    token.send_photo(chat_id=id, photo=open('Rating.jpg', 'rb'))


# duty
@token.message_handler(commands=["Дежурство"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, 'upload_photo')
    token.send_message(id, "Дежурство:\n")
    token.send_photo(chat_id=id, photo=open('Duty.jpg', 'rb'))


"""
Adding \ disabling buttons code
@token.message_handler(commands=["add"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/author","/help")
    user_markup.row("/list")
    user_markup.row("/rz")
    token.send_message(message.from_user.id,"Клавиатура была включена.Что бы её выключить, используйте команду /stop"
    ,reply_markup=user_markup)
@token.message_handler(commands=["stop"])
def handle_text(message):
    hide_markup = telebot.types.ReplyKeyboardHide()
    token.send_message(message.from_user.id,"Клавиатура была убранна.Что бы её включить, используйте команду /add"
    ,reply_markup=hide_markup)
user_markup = telebot.types.ReplyKeyboardMarkup()
user_markup.row("/author", "/help")
user_markup.row("/list")
user_markup.row("/duty", "/rating")
user_markup.row("/rz", "/news")
"""


# back<-
@token.message_handler(commands=["Назад"])
def handle_text(message):
    global send_1, send_2, get_1, get_2, news_get, news_send, photo_get
    id = message.from_user.id
    token.send_chat_action(id, "typing")
    menu(message, "Назад")
    # closing all add\deleting actions
    send_1 = False
    send_2 = False
    news_get = False
    news_send = False
    photo_get = False


def bool_comparision(token, id, text):
    global send_1, send_2, get_1, get_2, news_get, news_send, str_add, photo_get
    token.send_chat_action(id, "typing")
    if send_1 is True:
        with open('week1.txt', 'w') as file:
            file.write(text)
        send_1 = False
        get_1 = False
        token.send_message(id, "<b>Домашнее задание было добавлено!</b>", parse_mode="HTML")
    if send_2 is True:
        with open('week2.txt', 'w') as file:
            file.write(text)
        send_2 = False
        get_2 = False
        token.send_message(id, "<b>Домашнее задание было добавлено!</b>", parse_mode="HTML")
    if news_send is True:
        with open('news.txt', 'w') as file:
            file.write(text)
        news_get = False
        news_send = False
        photo_get = True
        token.send_message(id, "<b>Новости былы добавлены!</b>", parse_mode="HTML")
        token.send_message(id, """
<i>Пришлите соответствующую картинку к тексту, иначе, напишите delete, после чего воспользуйтесь командой /Назад.</i>
""", parse_mode="HTML")
    if photo_get is True and text == "delete":
        os.remove("news.jpg")
        token.send_message(id, "<b>Картинка была удалена!</b>", parse_mode="HTML")
    elif text == pas_1:
        log("password 1", text)
        token.send_message(id, "<i>Введите домашнее задание для 1 группы.</i>", parse_mode="HTML")
        send_1 = True
        get_2 = True
    elif text == pas_2:
        log("password 2", text)
        token.send_message(id, "<i>Введите домашнее задание для 2 группы.</i>", parse_mode="HTML")
        send_2 = True
        get_2 = True
    elif text == pas_3:
        log("password 3", text)
        token.send_message(id, "<i>Введите новости лицея.</i>", parse_mode="HTML")
        news_send = True
        news_get = True
    elif text == "Дурак":
        token.send_message(id, "<b>Сам такой!</b>", parse_mode="HTML")


# another text
@token.message_handler(content_types=["text"])
def handle_text(message):
    global get_1, get_2, news_get, photo_get
    id = message.chat.id
    token.send_chat_action(id, "typing")
    text = message.text
    file_1 = open("week1.txt", "r")
    file_2 = open("week2.txt", "r")

    bool_comparision(token, id, text)
    if get_1 is False and get_2 is False and news_get is False and photo_get is False:
        for str1 in file_1:
            if str1.startswith(text):
                token.send_message(id, str1)
        for str2 in file_2:
            if str2.startswith(text):
                    token.send_message(id, str2)
    file_1.close()
    file_2.close()


# https://api.telegram.org/file/bot<token>/<file_path>
@token.message_handler(content_types=['photo'])
def photo(message):
    global photo_get
    id = message.chat.id
    token.send_chat_action(id, "upload_photo")
    file_path = "news"
    if photo_get is True:
        if os.path.exists(file_path + ".jpg"):
            os.remove("news.jpg")
        print('message.photo =', message.photo)
        fileID = message.photo[-1].file_id
        print('fileID =', fileID)
        file_info = token.get_file(fileID)
        print('file.file_path =', file_info.file_path)
        downloaded_file = token.download_file(file_info.file_path)
        with open("news.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        token.send_message(id, "<b>Картинка была добавлена!</b>", parse_mode="HTML")
    photo_get = False


token.polling(none_stop=True)
