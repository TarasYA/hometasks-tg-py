"""
DZshnik...
"""
import telebot

bot = "785437577:AAG8e8aHRwd0toeTAqNExtIkaXmbtS5UZWs"
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

@token.message_handler(commands=["info"])
def handle_text(message):
    token.send_message(message.chat.id,"""
    Бот был создан учеником ЛИТа 8-В класса Яицким Тарасом.
    Вопросы? taras2005dn@gmail.com
    """)
@token.message_handler(commands=["start"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/info","/help")
    user_markup.row("/week1", "/week2")
    user_markup.row("/tomor1", "/tomor2")
    user_markup.row("/rz","/stop")
    token.send_message(message.chat.id, """
        Добро пожаловать!
        """,reply_markup=user_markup)

@token.message_handler(commands=["week1"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_document')
    token.send_message(message.chat.id,"""
    Домашнее задание на неделю для 1 группы:\n
    """)
    token.send_chat_action(message.chat.id, 'upload_document')
@token.message_handler(commands=["week2"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_document')
    token.send_message(message.chat.id,"""
    Домашнее задание на неделю для 2 группы:\n
    """)
    token.send_chat_action(message.chat.id, 'upload_document')
@token.message_handler(commands=["tomor1"])
def handle_text(message):
    token.send_chat_action(message.chat.id,'upload_document')
    token.send_message(message.chat.id,"""
    Домашнее задание на завтра для 1 группы:\n
    """)
    token.send_chat_action(message.chat.id, 'upload_document')
@token.message_handler(commands=["tomor2"])
def handle_text(message):
    token.send_chat_action(message.chat.id, 'upload_document')
    token.send_message(message.chat.id,"""
    Домашнее задание на завтра для 2 группы:\n
    """)
    token.send_chat_action(message.chat.id, 'upload_document')
@token.message_handler(commands=["help"])
def handle_text(message):
    token.send_message(message.chat.id,"""
    start - начать взаимодействие  
    info - о боте 
    week1 - домашнее задание на неделю(первая группа)
    tomor1 - домашнее задание на завтра(первая группа)
    week2 - домашнее задание на неделю(вторая группа)
    tomor2 - домашнее задание на завтра(вторая группа)
    rz - расписание 
    help - список команд
    stop - убрать внутреннюю клавиатуру
    add - показать клавиатуру
    """)
@token.message_handler(commands=["rz"])
def handle_text(message):
    token.send_message(message.chat.id,"""
    Расписание:\n 
    """)
    token.send_photo(chat_id=message.chat.id, photo=open('C:\\Users\\x\\PycharmProjects\\Python_telegabot\\8v.png', 'rb'))
@token.message_handler(commands=["add"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/info","/help")
    user_markup.row("/week1", "/week2")
    user_markup.row("/tomor1", "/tomor2")
    user_markup.row("/rz","/stop")
    token.send_message(message.from_user.id,"Клавиатура была включена.Что бы её выключить, используйте команду /stop",reply_markup=user_markup)
@token.message_handler(commands=["stop"])
def handle_text(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    token.send_message(message.from_user.id,"Клавиатура была убранна.Что бы её включить, используйте команду /add",reply_markup=hide_markup)


@token.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text
    id = message.chat.id
    if(text == "Дурак"):
        token.send_message(id,"<b>Сам такой!</b>",parse_mode="HTML")


token.polling(none_stop=True, interval=0)
