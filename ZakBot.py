"""
Frazochnik...
"""
import telebot
import os

# environment variables
bot = os.getenv("TOKEN2")
password = os.getenv("PASSWORD4")
token = telebot.TeleBot(bot)
# command list
string_help = """
/Команды - список команд бота
/Автор - автор бота
/Угар - логично?
"""
send = False


# log Heroku messaging
def log(message, answer):
    from datetime import datetime
    print("Log-message: ", message, "\nLog-datetime: ", datetime.now, "\nLog-user: ", answer)


# start function
@token.message_handler(commands=["start"])
def handle_text(message):
    global string_help
    id = message.chat.id
    menu(message, "Даров")
    token.send_message(id, string_help)


# menu creator
def menu(message, text):
    id = message.chat.id
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/Автор", "/Команды")
    user_markup.row("/Угар")
    token.send_message(id, str(text), reply_markup=user_markup)


# authors command
@token.message_handler(commands=["Автор"])
def handle_text(message):
    id = message.chat.id
    token.send_message(id, """
Бот был создан каким-то ноунеймом,ну лан, я короч Лев Вакуленко(@superninjalguy).Ну и юзер-нейм, конечно.
Вопросы? 
2281337@gmail.com
lolkekcheburek@yandex.ua
orbidol@yandex.ru
""")


# commands info
@token.message_handler(commands=["Команды"])
def handle_text(message):
    global string_help
    id = message.chat.id
    token.send_message(id, string_help)


@token.message_handler(commands=["Угар"])
def handle_text(message):
    id = message.chat.id
    token.send_message(id, "Список фраз:")
    file = open("fun.txt", "r")
    for s in file:
        token.send_message(id, s)


@token.message_handler(commands=["Назад"])
def handle_text(message):
    global send
    id = message.chat.id
    token.send_message(id, "Назад")
    send = False


@token.message_handler(content_types=["text"])
def handle_text(message):
    global send
    token.send_chat_action(message.chat.id, "typing")
    text = message.text
    id = message.chat.id

    if(send == True):
        with open('fun.txt', 'w') as file:
            file.write(text)
        token.send_message(id, "<b>Порция угара была добавлена!Упссс... Слишком много слова угар. Ахх, снова!11!1</b>",
                           parse_mode="HTML")
    if(text == password):
        token.send_message(id, "<i>Введите угарную фразочку, иначе, воспользуйтесь командой /Назад</i>", parse_mode="HTML")
        send = True
        log("password", "sending = True")


token.polling(none_stop=True)
