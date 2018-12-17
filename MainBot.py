"""
DZshnik...
"""
import telebot
import os

bot = os.getenv("TOKEN")
pas_1 = os.getenv("PASSWORD")
pas_2 = os.getenv("PASSWORD2")
token = telebot.TeleBot(bot)
get_1 = False
get_2 = False
send_1 = False
send_2 = False
get_text_1 = False
get_text_2 = False
str_add = ""
#token.send_message(402702337,"test")
#upd = token.get_updates()
#print(upd)
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

print(token.get_me())

def log(message, answer):
    from datetime import datetime
    print("Log-message: ", message, "\nLog-datetime: ", datetime.now, "\nLog-user: ",answer)


@token.message_handler(commands=["author"])
def handle_text(message):
    token.send_message(message.chat.id, """
    Бот был создан учениками ЛИТа 8-В класса Яицким Тарасом, Антоном Мордаком, Хорсуном Дмитрием.
Вопросы? 
taras2005dn@gmail.com
frieddimka@gmail.com
antongimnasium@gmail.com
""")
@token.message_handler(commands=["start"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/author", "/help")
    user_markup.row("/list")
    user_markup.row("/duty", "/rating")
    user_markup.row("/rz", "/news")
    token.send_message(message.chat.id, """
        Добро пожаловать!
        """,reply_markup=user_markup)
    token.send_message(message.chat.id, """
start - начать взаимодействие  
author - о боте 
list - домашнее задание 
rz - расписание 
help - список команд
duty - дежурство
rating - рейтинг
news - новости
""")
@token.message_handler(commands=["list"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("ukr.lit", "for.lit")
    user_markup.row("urk.m","rus.m","en.m")
    user_markup.row("math", "physics", "informatics")
    user_markup.row("chemistry", "geography", "history")
    user_markup.row("art", "bio", "/back")
    token.send_message(message.from_user.id, "Список предметов",reply_markup=user_markup)
@token.message_handler(commands=["help"])
def handle_text(message):
    token.send_message(message.chat.id, """
start - начать взаимодействие  
author - о боте 
list - домашнее задание 
rz - расписание 
help - список команд
duty - дежурство
rating - рейтинг
""")
@token.message_handler(commands=["rz"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    token.send_message(message.chat.id, """
    Расписание:\n""")
    token.send_photo(chat_id=message.chat.id, photo=open('8v.png', 'rb'))
@token.message_handler(commands=["news"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    file_path = "news"
    token.send_message(message.chat.id, """
    Новости:\n """)
    token.send_photo(chat_id=message.chat.id, photo=open('news.png', 'rb'))
    if(os.path.exists(file_path + ".png")):
        file = open(file_path + ".png", "r")
        for s in file:
            token.send_message(message.from_user.id, s)
        file.close()
    elif(os.path.exists(file_path + ".jpg")):
        file = open(file_path + ".jpg", "r")
        for s in file:
            token.send_message(message.from_user.id, s)
        file.close()
    else:
        token.send_message(message.from_user.id, "Новостей нет!")
@token.message_handler(commands=["rating"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    token.send_message(message.from_user.id,"Рейтинг:\n")
    token.send_photo(chat_id=message.chat.id, photo=open('media-share-0-02-04-13249eda0fb4da7090711a1abf81653171baa9ad34c602a824e77363d908888c-f12d5cea-2570-4c63-b527-959d0dac5d66.jpg', 'rb'))
@token.message_handler(commands=["duty"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    token.send_message(message.from_user.id,"Дежурство:\n")
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
"""

@token.message_handler(commands=["back"])
def handle_text(message):
    global send_1,send_2,get_1,get_2
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/author", "/help")
    user_markup.row("/list")
    user_markup.row("/duty","/rating")
    user_markup.row("/rz","/news")
    token.send_message(message.from_user.id,"Назад",reply_markup=user_markup)
    send_1 = False
    send_2 = False
    get_1 = False
    get_2 = False
@token.message_handler(content_types=["text"])
def handle_text(message):
    global get_1,get_2,send_1,send_2,get_text_1,get_text_2,str_add
    token.send_chat_action(message.chat.id, "typing")
    text = message.text
    id = message.chat.id
    file_1 = open("week1.txt","r+")
    file_2 = open("week2.txt","r+")

    if(send_1 == True):
        file_1.write(text)
        send_1 = False
        get_1 = False
        token.send_message(id, "<b>Домашнее задание было добавлено!</b>", parse_mode="HTML")
    if (send_2 == True):
        file_2.write(text)
        send_2 = False
        get_2 = False
        token.send_message(id, "<b>Домашнее задание было добавлено!</b>", parse_mode="HTML")
    elif (text == pas_1):
        log("password 1", text)
        token.send_message(id, "<i>Введите домашнее задание для 1 группы.</i>", parse_mode="HTML")
        send_1 = True
        get_1 = True
    elif (text == pas_2):
        log("password 2", text)
        token.send_message(id, "<i>Введите домашнее задание для 2 группы.</i>", parse_mode="HTML")
        send_2 = True
        get_2 = True
    elif(text == "Дурак"):
        token.send_message(id,"<b>Сам такой!</b>",parse_mode="HTML")

    file_1.close()
    file_2.close()
    file_1 = open("week1.txt", "r+")
    file_2 = open("week2.txt", "r+")

    for s in file_1:
        if(get_1 != True):
            if (s.startswith(text)):
                token.send_message(message.from_user.id, s)
        for s2 in file_2:
            if(get_2 != True):
                if(s2.startswith(text)):
                    token.send_message(message.from_user.id, s2)

    file_1.close()
    file_2.close()

token.polling(none_stop=True, interval=0)
