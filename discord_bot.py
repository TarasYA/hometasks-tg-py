"""
Discorder...
"""
import os
from discord.ext import commands


TOKEN = os.getenv("distok")
CLIENT = commands.Bot(command_prefix="m!")


@CLIENT.event
async def on_ready():
    """
    bot started working
    """
    print("running")


@CLIENT.event
async def on_member_join(member):
    """
    when new member join
    """
    file = open("DiscordServerNames.txt", "r+")
    for channel in member.server.channels:
        if channel.name == "test":
            string = f"""
Привет, + {str({member.name})}!
Зарегистрируйтесь, используя команду m!reg nickname(только слитно) realname.
Если, на нашем сервере у Вас больше чем 1 аккаунт, напишите никнеймы через запятую без пробела.
Используйте команду m!commands для того что бы узнать все команды бота.
"""
            await CLIENT.send_message(channel, string)
        if channel.name == 'names':
            amount = 50
            messages = []
            async for message in CLIENT.logs_from(channel, limit=int(amount) + 1):
                messages.append(message)
            await CLIENT.delete_messages(messages)
            await CLIENT.send_message(channel, "|==================================|")
            for line in file:
                await CLIENT.send_message(channel, line)
            await CLIENT.send_message(channel, "|==================================|")
    file.close()


@CLIENT.command(pass_context=True)
async def info(ctx):
    """
    info about server
    """
    channel = ctx.message.channel
    await CLIENT.send_message(channel, """Сервер для фолс программистов от тру быдлокодеров...""")


@CLIENT.command(pass_context=True)
async def lol(ctx):
    """
    test
    """
    channel = ctx.message.channel
    await CLIENT.send_message(channel, "kek")


@CLIENT.command(pass_context=True)
async def command(ctx):
    """
    list of commands
    """
    channel = ctx.message.channel
    await CLIENT.send_message(channel, """
Список команд:
m!reg nickname realname - регистрация на сервере;
m!clear count - стирание текста на сервере;
m!info - информация о сервере;
m!names - имена людей на сервере;
m!command - команды на сервере.
""")


@CLIENT.command(pass_context=True)
async def reg(ctx, nickname, realname):
    """
    register on server
    """
    channel = ctx.message.channel
    nickname = str(nickname)
    realname = str(realname)
    msg = "\n" + nickname + "-" + realname
    if len(msg) > 20:
        await CLIENT.send_message(channel, "Слишком большие входные данные!")
    else:
        with open("DiscordServerNames.txt", 'a') as file:
            file.writelines(msg)
        await CLIENT.send_message(channel, "Спасибо за регистрацию!")
        file.close()


@CLIENT.command(pass_context=True)
async def names(ctx):
    """
    list of names in server
    """
    file = open("DiscordServerNames.txt", "r+")
    channel = ctx.message.channel
    for line in file:
        await CLIENT.send_message(channel, line)
    file.close()


@CLIENT.command(pass_context=True)
async def clear(ctx, amount=100):
    """
    chat clearing
    """
    channel = ctx.message.channel

    if amount >= 2:
        messages = []
        async for message in CLIENT.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await CLIENT.delete_messages(messages)
    else:
        await CLIENT.send_message(channel, "Введите значение которое равно или больше 2!")

CLIENT.run(TOKEN)
print('stopped')
