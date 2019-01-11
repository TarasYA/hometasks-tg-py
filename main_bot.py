"""
DZshnik...
"""
import os
import telebot
from dropboxing import downloading_file, upload_file, deleting_file, checking_exist

# environment variables
BOT = os.getenv("TOKEN")
PAS_1 = os.getenv("PASSWORD")
PAS_2 = os.getenv("PASSWORD2")
TOKEN = telebot.TeleBot(BOT)
# action send\get bool variables
GET_1 = False
GET_2 = False
SEND_1 = False
SEND_2 = False
NEWS_GET = False
NEWS_SEND = False
PHOTO_GET = False
# command list
STR_HELP = """
start - начать взаимодействие или включить клавиатуру 
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

print(TOKEN.get_me())


def log(message, answer):
    """
    Heroku logging
    """
    from datetime import datetime
    print("Log-message: ", message, "\nLog-datetime: ", datetime.now, "\nLog-user: ", answer)


def admin(message_id, send, parse="HTML"):
    """
    default menu
    """
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("Добавить дз", "Добавить новости")
    user_markup.row("/Назад")
    TOKEN.send_message(message_id, str(send), reply_markup=user_markup, parse_mode=parse)


def menu(message, send):
    """
    admin menu
    """
    message_id = message.chat.id
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("/Авторы", "/Команды")
    user_markup.row("/Список_дз", "/Всё_дз")
    user_markup.row("/Дежурство", "/Рейтинг")
    user_markup.row("/Расписание", "/Новости")
    TOKEN.send_message(message_id, str(send), reply_markup=user_markup)


@TOKEN.message_handler(commands=["start"])
def start(message):
    """
    start function
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    menu(message, "Вас приветствует лицейский бот 8-В класса."
                  " Используя команды ниже, узнайте нужную Вам информацию. Удачи!")
    TOKEN.send_message(message_id, STR_HELP)


@TOKEN.message_handler(commands=["Авторы"])
def authors(message):
    """
    get authors
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    TOKEN.send_message(message_id, """
Бот был создан учениками ЛИТа 8-В класса Яицким Тарасом, Антоном Мордаком, Хорсуном Дмитрием.
Вопросы? 
taras2005dn@gmail.com
frieddimka@gmail.com
antongimnasium@gmail.com
""")


@TOKEN.message_handler(commands=["Команды"])
def commands(message):
    """
    commands info
    """
    message_id = message.chat.id
    TOKEN.send_message(message_id, STR_HELP)


@TOKEN.message_handler(commands=["Список_дз"])
def list_homework(message):
    """
    list of homework
    """
    message_id = message.chat.id
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("ukr.lit", "for.lit")
    user_markup.row("urk.m", "rus.m", "en.m")
    user_markup.row("math", "physics", "informatics")
    user_markup.row("chemistry", "geography", "history")
    user_markup.row("art", "bio", "/Назад")
    TOKEN.send_message(message_id, "Список предметов", reply_markup=user_markup)


@TOKEN.message_handler(commands=["Всё_дз"])
def all_homework(message):
    """
    all homework
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    downloading_file("week1.txt")
    downloading_file("week2.txt")
    file_1 = open("week1.txt", "r+")
    file_2 = open("week2.txt", "r+")
    str_default = "|!=---{0} группа---=!|"

    if GET_1 is False and GET_1 is False and NEWS_GET is False:
        TOKEN.send_message(message_id, str_default.format(1))
        list1 = [TOKEN.send_message(message_id, string) for string in file_1]
        del list1
        TOKEN.send_message(message_id, str_default.format(2))
        list2 = [TOKEN.send_message(message_id, string) for string in file_2]
        del list2

    file_1.close()
    file_2.close()


@TOKEN.message_handler(commands=["Расписание"])
def subject_list(message):
    """
    subject list
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, 'upload_photo')
    TOKEN.send_message(message_id, """
    Расписание:\n""")
    TOKEN.send_photo(chat_id=message_id, photo=open('8v.png', 'rb'))


@TOKEN.message_handler(commands=["Новости"])
def news_list(message):
    """
    lyceum news list
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, 'upload_photo')
    file_path = "news"
    TOKEN.send_message(message_id, """
    Новости:\n """)

    if checking_exist(file_path + ".jpg"):
        downloading_file(file_path + ".jpg")
        TOKEN.send_photo(chat_id=message_id, photo=open(file_path + ".jpg", 'rb'))
    if os.path.exists("news.txt"):
        downloading_file("news.txt")
        file = open("news.txt", "r")
        list_news = [TOKEN.send_message(message_id, line) for line in file]
        del list_news
        file.close()
    else:
        TOKEN.send_message(message_id, "Новостей нет!")


@TOKEN.message_handler(commands=["Рейтинг"])
def rating_list(message):
    """
    rating list
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, 'upload_photo')
    TOKEN.send_message(message_id, "Рейтинг:\n")
    TOKEN.send_photo(chat_id=message_id, photo=open('Rating.jpg', 'rb'))


@TOKEN.message_handler(commands=["Дежурство"])
def duty_list(message):
    """
    duty list
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, 'upload_photo')
    TOKEN.send_message(message_id, "Дежурство:\n")
    TOKEN.send_photo(chat_id=message_id, photo=open('Duty.jpg', 'rb'))


@TOKEN.message_handler(commands=["Назад"])
def back(message):
    """
    back<- to the default menu
    """
    global SEND_1, SEND_2, NEWS_SEND, PHOTO_GET
    message_id = message.from_user.id
    TOKEN.send_chat_action(message_id, "typing")

    if SEND_1 is False and SEND_2 is False and NEWS_SEND is False and PHOTO_GET is False:
        menu(message, "Назад")
        log("menu", "menu")
    else:
        admin(message, "<i>Нажмите назад ещё раз, если Вы хотите выйте из админской панели.</i>")
        log("admin menu", "admin menu")
    # closing all add\deleting actions
    SEND_1 = False
    SEND_2 = False
    NEWS_SEND = False
    PHOTO_GET = False


def bool_comparision(message_id, text):
    """
    bool comparision
    """
    global SEND_1, SEND_2, GET_1, GET_2, NEWS_GET, NEWS_SEND, PHOTO_GET
    home_add = "<i>Введите домашнее задание для {0} группы, иначе, " \
               "воспользуйтесь командой /Назад.</i>"
    home_got = "<b>Домашнее задание было добавлено!</b>"
    TOKEN.send_chat_action(message_id, "typing")

    if GET_1 is True and text == "Добавить дз":
        SEND_1 = True
    if GET_2 is True and text == "Добавить дз":
        SEND_2 = True
    if GET_1 is True or GET_2 is True and text == "Добавить новости":
        NEWS_SEND = True
    if SEND_1 is True and text != "Добавить дз":
        with open('week1.txt', 'w') as file:
            file.write(text)
        SEND_1 = False
        GET_1 = False
        upload_file("week1.txt")
        TOKEN.send_message(message_id, home_got, parse_mode="HTML")
    if SEND_2 is True and text != "Добавить дз":
        with open('week2.txt', 'w') as file:
            file.write(text)
        SEND_2 = False
        GET_1 = False
        upload_file("week2.txt")
        TOKEN.send_message(message_id, home_got, parse_mode="HTML")
    if NEWS_SEND is True and text != "Добавить новости":
        with open('news.txt', 'w') as file:
            file.write(text)
        NEWS_GET = False
        NEWS_SEND = False
        PHOTO_GET = True
        upload_file("news.txt")
        TOKEN.send_message(message_id, "<b>Новости былы добавлены!</b>", parse_mode="HTML")
        TOKEN.send_message(message_id, """
<i>Пришлите соответствующую картинку к тексту, иначе, напишите delete, после чего воспользуйтесь командой /Назад.</i>
""", parse_mode="HTML")
    if PHOTO_GET is True and text == "delete":
        os.remove("news.jpg")
        deleting_file("news.jpg")
        TOKEN.send_message(message_id, "<b>Картинка была удалена!</b>", parse_mode="HTML")
        PHOTO_GET = False
    elif text == PAS_1:
        log("password 1", text)
        GET_1 = True
        admin(message_id, "Админская панель")
    elif text == PAS_2:
        log("password 2", text)
        GET_2 = True
        admin(message_id, "Админская панель")
    elif text == "Дурак":
        TOKEN.send_message(message_id, "<b>Сам такой!</b>", parse_mode="HTML")


@TOKEN.message_handler(content_types=["text"])
def handle_text(message):
    """
    another (not command) text
    """
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "typing")
    text = message.text
    downloading_file("week1.txt")
    downloading_file("week2.txt")
    file_1 = open("week1.txt", "r")
    file_2 = open("week2.txt", "r")

    bool_comparision(message_id, text)
    if GET_1 is False and GET_1 is False and NEWS_GET is False and PHOTO_GET is False:
        list1 = [TOKEN.send_message(message_id, string) for string in file_1
                 if string.startswith(text) is True]
        del list1
        list2 = [TOKEN.send_message(message_id, string) for string in file_2
                 if string.startswith(text) is True]
        del list2

    file_1.close()
    file_2.close()


@TOKEN.message_handler(content_types=['photo'])
def get_photo(message):
    """
    https://api.telegram.org/file/bot<token>/<file_path>
    loading photo
    """
    global PHOTO_GET
    message_id = message.chat.id
    TOKEN.send_chat_action(message_id, "upload_photo")
    file_path = "news"

    if PHOTO_GET is True:
        if os.path.exists(file_path + ".jpg"):
            os.remove("news.jpg")
        print('message.photo =', message.photo)
        file_id = message.photo[-1].file_id
        print('fileID =', file_id)
        file_info = TOKEN.get_file(file_id)
        print('file.file_path =', file_info.file_path)
        downloaded_file = TOKEN.download_file(file_info.file_path)
        with open("news.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
            TOKEN.send_message(message_id, "<b>Картинка была добавлена!</b>", parse_mode="HTML")
    PHOTO_GET = False


TOKEN.infinity_polling(True)
