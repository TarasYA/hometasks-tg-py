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
str_add = ""
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
#token.send_message(402702337,"test")
#upd = token.get_updates()
#print(upd)
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

print(token.get_me())

def log(message, answer):
    from datetime import datetime
    print("Log-message: ", message, "\nLog-datetime: ", datetime.now, "\nLog-user: ", answer)


@token.message_handler(commands=["Авторы"])
def handle_text(message):
    token.send_message(message.chat.id, """
    Бот был создан учениками ЛИТа 8-В класса Яицким Тарасом, Антоном Мордаком, Хорсуном Дмитрием.
Вопросы? 
taras2005dn@gmail.com
frieddimka@gmail.com
antongimnasium@gmail.com
""")

def menu(message, send):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/Авторы", "/Команды")
    user_markup.row("/Список_дз", "/Всё_дз")
    user_markup.row("/Дежурство", "/Рейтинг")
    user_markup.row("/Расписание", "/Новости")
    token.send_message(message.from_user.id, str(send), reply_markup=user_markup)

@token.message_handler(commands=["start"])
def handle_text(message):
    global string_help
    menu(message, "Добро пожаловать!")
    token.send_message(message.chat.id, string_help)

@token.message_handler(commands=["Команды"])
def handle_text(message):
    global string_help
    token.send_message(message.chat.id,string_help)

@token.message_handler(commands=["Список_дз"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("ukr.lit", "for.lit")
    user_markup.row("urk.m", "rus.m", "en.m")
    user_markup.row("math", "physics", "informatics")
    user_markup.row("chemistry", "geography", "history")
    user_markup.row("art", "bio", "/Назад")
    token.send_message(message.from_user.id, "Список предметов", reply_markup=user_markup)

@token.message_handler(commands=["Всё_дз"])
def handle_text(message):
    global get_1, get_2, news_get
    file_1 = open("week1.txt", "r+")
    file_2 = open("week2.txt", "r+")
    if(get_1 == False and get_2 == False and news_get == False):
        for str1 in file_1:
            token.send_message(message.from_user.id, str1)
        for str2 in file_2:
            token.send_message(message.from_user.id, str2)
    file_1.close()
    file_2.close()

@token.message_handler(commands=["Расписание"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    token.send_message(message.chat.id, """
    Расписание:\n""")
    token.send_photo(chat_id=message.chat.id, photo=open('8v.png', 'rb'))

@token.message_handler(commands=["Новости"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    file_path = "news"
    token.send_message(message.chat.id, """
    Новости:\n """)
    if(os.path.exists(file_path + ".png")):
        token.send_photo(chat_id=message.chat.id, photo=open(file_path + ".png", 'rb'))
        file = open("news.txt", "r")
        for s in file:
            token.send_message(message.from_user.id, s)
    elif(os.path.exists(file_path + ".jpg")):
        token.send_photo(chat_id=message.chat.id, photo=open(file_path + ".jpg", 'rb'))
        file = open("news.txt", "r")
        for s in file:
            token.send_message(message.from_user.id, s)
        file.close()
    elif(os.path.exists("news.txt")):
        file = open("news.txt", "r")
        for s in file:
            token.send_message(message.from_user.id, s)
        file.close()
    else:
        token.send_message(message.from_user.id, "Новостей нет!")

@token.message_handler(commands=["Рейтинг"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    token.send_message(message.from_user.id, "Рейтинг:\n")
    token.send_photo(chat_id=message.chat.id, photo=open('Rating.jpg', 'rb'))

@token.message_handler(commands=["Дежурство"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    token.send_message(message.from_user.id, "Дежурство:\n")
    token.send_photo(chat_id=message.chat.id, photo=open('Duty.jpg', 'rb'))

"""
Adding \ disabling buttons code

@token.message_handler(commands=["add"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/author","/help")
    user_markup.row("/list")
    user_markup.row("/rz")
    token.send_message(message.from_user.id,"Клавиатура была включена.Что бы её выключить, используйте команду /stop",reply_markup=user_markup)
@token.message_handler(commands=["stop"])
def handle_text(message):
    hide_markup = telebot.types.ReplyKeyboardHide()
    token.send_message(message.from_user.id,"Клавиатура была убранна.Что бы её включить, используйте команду /add",reply_markup=hide_markup)
user_markup = telebot.types.ReplyKeyboardMarkup()
user_markup.row("/author", "/help")
user_markup.row("/list")
user_markup.row("/duty", "/rating")
user_markup.row("/rz", "/news")
"""

@token.message_handler(commands=["Назад"])
def handle_text(message):
    global send_1, send_2, get_1, get_2, news_get, news_send
    menu(message, "Назад")
    send_1 = False
    send_2 = False
    news_get = False
    news_send = False

@token.message_handler(content_types=["text"])
def handle_text(message):
    global send_1, send_2, get_1, get_2, news_get, news_send, str_add
    token.send_chat_action(message.chat.id, "typing")
    text = message.text
    id = message.chat.id

    if(send_1 == True):
        with open('week1.txt', 'w') as file:
            file.write(text)
        send_1 = False
        get_1 = False
        token.send_message(id, "<b>Домашнее задание было добавлено!</b>", parse_mode="HTML")
    if (send_2 == True):
        with open('week2.txt', 'w') as file:
            file.write(text)
        send_2 = False
        get_2 = False
        token.send_message(id, "<b>Домашнее задание было добавлено!</b>", parse_mode="HTML")
    if(news_send == True):
        file_3.write(text)
        news_get = False
        news_send = False
        token.send_message(id, "<b>Новости былы добавлены!</b>", parse_mode="HTML")
    elif (text == pas_1):
        log("password 1", text)
        token.send_message(id, "<i>Введите домашнее задание для 1 группы.</i>", parse_mode="HTML")
        send_1 = True
        get_2 = True
    elif (text == pas_2):
        log("password 2", text)
        token.send_message(id, "<i>Введите домашнее задание для 2 группы.</i>", parse_mode="HTML")
        send_2 = True
        get_2 = True
    elif(text == pas_3):
        log("password 3", text)
        token.send_message(id, "<i>Введите новости лицея.</i>", parse_mode="HTML")
        news_send = True
        news_get = True
    elif(text == "Дурак"):
        token.send_message(id, "<b>Сам такой!</b>", parse_mode="HTML")

    file_1 = open("week1.txt", "r")
    file_2 = open("week2.txt", "r")
    file_3 = open("news.txt", "w")
    if (get_1 == False and get_2 == False and news_get == False):
        for str1 in file_1:
            if(str1.startswith(text)):
                token.send_message(message.from_user.id, str1)
            for str2 in file_2:
                if(str2.startswith(text)):
                    token.send_message(message.from_user.id, str2)
    file_1.close()
    file_2.close()
    file_3.close()


token.polling(none_stop=True)
