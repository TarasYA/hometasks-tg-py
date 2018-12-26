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
/Commands - список команд бота
/Author - автор бота
/Fun - логично?
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
    token.send_chat_action(id, "typing")
    menu(message, "Даров")
    token.send_message(id, string_help)


# menu creator
def menu(message, text):
    id = message.chat.id
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/Author", "/Commands")
    user_markup.row("/Fun")
    token.send_message(id, str(text), reply_markup=user_markup)


# authors command
@token.message_handler(commands=["Author"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, """
Бот был создан каким-то ноунеймом,ну лан, я короч Лев Вакуленко(@superninjalguy).Ну и юзер-нейм странный, конечно.
Почта: 
2281337@gmail.com
lolkekcheburek@yandex.ua
orbidol@yandex.ru
""")


# commands info
@token.message_handler(commands=["Commands"])
def handle_text(message):
    global string_help
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, string_help)


@token.message_handler(commands=["Fun"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, "Список фраз:")
    file = open("fun.txt", "r")
    for s in file:
        token.send_message(id, s)


@token.message_handler(commands=["Back"])
def handle_text(message):
    global send
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, "Назад")
    send = False


@token.message_handler(content_types=["text"])
def handle_text(message):
    global send
    text = message.text
    id = message.chat.id
    token.send_chat_action(id, "typing")

    if(send is True and not text.startwith("delete")):
        with open('fun.txt', 'w') as file:
            file.write(text)
        token.send_message(id, "<b>Порция угара была добавлена!Упссс... Слишком много слова угар. Ахх, снова!11!1</b>",
                           parse_mode="HTML")
        send = False
    if(send is True and text.startwith("delete")):
       string = text.split("\n")
       print(string)
       final_string = " "
       f = open('fun.txt', 'r')
       for line in f:
           if(line not in != string): final_string += line + "\n"
       print(final_string)
  
    if(text == password):
        token.send_message(id, "<i>Введите угарную фразочку\удалите уже существующую, иначе, воспользуйтесь командой /Back</i>", parse_mode="HTML")
        send = True
        log("password", "sending = True")
    if(text.lower() == "каламбот"):
        token.send_message(id, "Чё нада:??")


token.polling(none_stop=True)
