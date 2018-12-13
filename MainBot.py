"""
DZshnik...
"""
import telebot
import os

bot = os.getenv("TOKEN")
token = telebot.TeleBot(bot)

#token.send_message(402702337,"test")
#upd = token.get_updates()
#print(upd)
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

print(token.get_me())
"""
def log(message, answer):
    from datetime import datetime
    print("Log-message: ", message.text,"\nLog-datetime: ", datetime.now, "\nLog-user: ",message.from_user.first_name)
"""

@token.message_handler(commands=["author"])
def handle_text(message):
    token.send_message(message.chat.id,"""
    Бот был создан учеником ЛИТа 8-В класса Яицким Тарасом.
Вопросы? taras2005dn@gmail.com
    """)
@token.message_handler(commands=["start"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/author","/help")
    user_markup.row("/list")
    user_markup.row("/rz")
    token.send_message(message.chat.id, """
        Добро пожаловать!
        """,reply_markup=user_markup)
    token.send_message(message.chat.id, """
start - начать взаимодействие  
author - о боте 
list - домашнее задание 
rz - расписание 
help - список команд
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
    token.send_message(message.chat.id,"""
start - начать взаимодействие  
author - о боте 
list - домашнее задание 
rz - расписание 
help - список команд
stop - убрать внутреннюю клавиатуру
add - показать клавиатуру
    """)
@token.message_handler(commands=["rz"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_photo')
    token.send_message(message.chat.id,"""
    Расписание:\n 
    """)
    token.send_photo(chat_id=message.chat.id, photo=open('8v.png', 'rb'))
"""
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
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/author", "/help")
    user_markup.row("/list")
    user_markup.row("/rz")
    token.send_message(message.from_user.id,"Назад",reply_markup=user_markup)


@token.message_handler(content_types=["text"])
def handle_text(message):
    token.send_chat_action(message.chat.id, "typing")
    text = message.text
    id = message.chat.id

    if(text == "Дурак"):
        token.send_message(id,"<b>Сам такой!</b>",parse_mode="HTML")

    file = open("week.txt","r+")
    for s in file:
        if(s.startswith(text)):
            token.send_message(message.from_user.id, s)
    file.close()

token.polling(none_stop=True, interval=0)
