"""
Frazochnik...
"""
import os
import telebot

# environment variables
BOT = os.getenv("TOKEN2")
PASSWORD = os.getenv("PASSWORD4")
TOKEN = telebot.TeleBot(BOT)
# command list
STR_HELP = """
/start - начать взаимодействие или включить клавиатуру
/commands - список команд бота
/author - автор бота
/fun - логично?
"""
# bool sendable variable
SEND = False


def log(message, answer):
    """
    Heroku logging
    """
    from datetime import datetime
    print("Log-message: ", message, "\nLog-datetime: ", datetime.now, "\nLog-user: ", answer)


@TOKEN.message_handler(commands=["start"])
def start(message):
    """
    start function
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    menu(message, "Даров")
    TOKEN.send_message(message_id, STR_HELP)


def menu(message, text):
    """
    menu creator
    """
    message_id = message.chat.id
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/author", "/commands")
    user_markup.row("/fun")
    TOKEN.send_message(message_id, str(text), reply_markup=user_markup)


@TOKEN.message_handler(commands=["author"])
def author(message):
    """
    get author
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    TOKEN.send_message(message_id, """
Бот был создан каким-то ноунеймом, ну лан, я короч Лев Вакуленко(@superninjalguy).Ну и юзер-нейм странный, конечно.
Почта: 
2281337@gmail.com
lolkekcheburek@yandex.ua
orbidol@yandex.ru
""")


@TOKEN.message_handler(commands=["commands"])
def commands(message):
    """
    commands info
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    TOKEN.send_message(message_id, STR_HELP)


@TOKEN.message_handler(commands=["fun"])
def fun(message):
    """
    fun sending
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    TOKEN.send_message(message_id, "Список фраз:")
    file = open("fun.txt", "r")
    for line in file:
        TOKEN.send_message(message_id, line)
    file.close()


@TOKEN.message_handler(commands=["back"])
def back(message):
    """
    back<- to the default menu
    """
    global SEND
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    TOKEN.send_message(message_id, "Назад")
    SEND = False


@TOKEN.message_handler(content_types=["text"])
def handle_text(message):
    """
    another (not command) text
    """
    global SEND
    text = message.text
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")

    if SEND is True and not text.startswith("delete"):
        with open('fun.txt', 'a') as file:
            file.write(str(text + "\n"))
            print(text)
        string = "<b>Порция угара была добавлена!Упссс... Слишком много слова угар." \
                 "Ахх, снова!11!1</b>"
        TOKEN.send_message(message_id, string, parse_mode="HTML")
        SEND = False
    if SEND is True and text.startswith("delete"):
        words = text.split("\n")
        final_string = ""
        file = open('fun.txt', 'r', encoding="utf-8")
        for line in file:
            line = line.strip()
            if line not in words and len(line) > 2:
                final_string += line + "\n"
        file.close()
        print(words)
        with open('fun.txt', 'w') as file:
            file.write(final_string)
        SEND = False
        string = "<b>Килограм угара был убран!Эхх, старые мемы уходят, а им на замен " \
                 "приходят новые.Жестокие реалии нашего мира...</b>"
        TOKEN.send_message(message_id, string, parse_mode="HTML")
    if text == PASSWORD:
        string = "<i>Введите угарную фразочку или удалите уже существующую, иначе, " \
                 "воспользуйтесь командой /back</i>"
        TOKEN.send_message(message_id, string, parse_mode="HTML")
        SEND = True
        log("password", "sending = True")
    if text.lower() == "каламбот":
        TOKEN.send_message(message_id, "Чё нада:??")


TOKEN.polling(none_stop=True)
