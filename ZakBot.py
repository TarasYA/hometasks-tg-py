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
/commands - список команд бота
/author - автор бота
/fun - логично?
"""
# bool sendable variable
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
    user_markup.row("/author", "/commands")
    user_markup.row("/fun")
    token.send_message(id, str(text), reply_markup=user_markup)


# authors command
@token.message_handler(commands=["author"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, """
Бот был создан каким-то ноунеймом, ну лан, я короч Лев Вакуленко(@superninjalguy).Ну и юзер-нейм странный, конечно.
Почта: 
2281337@gmail.com
lolkekcheburek@yandex.ua
orbidol@yandex.ru
""")



# commands info
@token.message_handler(commands=["commands"])
def handle_text(message):
    global string_help
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, string_help)


# fun sending
@token.message_handler(commands=["fun"])
def handle_text(message):
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, "Список фраз:")
    file = open("fun.txt", "r")
    for s in file:
        try:
            token.send_message(id, s)
        except Exception:
            pass
    file.close()


# <- back to the default menu
@token.message_handler(commands=["back"])
def handle_text(message):
    global send
    id = message.chat.id
    token.send_chat_action(id, "typing")
    token.send_message(id, "Назад")
    send = False


# another text
@token.message_handler(content_types=["text"])
def handle_text(message):
    global send
    text = message.text
    id = message.chat.id
    token.send_chat_action(id, "typing")

    if(send is True and not text.startswith("delete")):
        with open('fun.txt', 'a') as file:
            file.write(str(text + "\n"))
            print(text)
        token.send_message(id, "<b>Порция угара была добавлена!Упссс... Слишком много слова угар."
                               "Ахх, снова!11!1</b>", parse_mode="HTML")
        send = False
    if(send is True and text.startswith("delete")):
        words = text.split("\n")
        final_string = ""
        f = open('fun.txt', 'r', encoding="utf-8")
        for line in f:
            line = line.strip()
            if line not in words and len(line) > 2:
                final_string += line + "\n"
        f.close()
        print(words)
        with open('fun.txt', 'w') as file:
            file.write(final_string)
        send = False
        token.send_message(id, "<b>Килограм угара был убран!Эхх, старые мемы уходят, а им на замен приходят новые."
                               "Жестокие реалии нашего мира...</b>", parse_mode="HTML")

    if(text == password):
        token.send_message(id, "<i>Введите угарную фразочку\удалите уже существующую, иначе, воспользуйтесь командой "
                               "/back</i>", parse_mode="HTML")
        send = True
        log("password", "sending = True")
    if(text.lower() == "каламбот"):
        token.send_message(id, "Чё нада:??")


token.polling(none_stop=True)
