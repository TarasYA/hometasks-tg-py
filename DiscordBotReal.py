"""
Personal by me.
"""
import discord
import os
from discord.ext import commands

token = os.getenv("distok")
client = commands.Bot(command_prefix="m!")

file = open("DiscordServerNames.txt", "r+")


@client.event
async def on_ready():
    print("running")


@client.event
async def on_member_join(member):
    file = open("DiscordServerNames.txt", "r+")
    messages = []
    for channel in member.server.channels:
        if channel.name == "test":
            await client.send_message(channel, "Привет, " + str(member.name) + "!")
            await client.send_message(channel, "Зарегистрируйтесь, используя команду m!reg nickname(только слитно) realname.")
            await client.send_message(channel, "Если, на нашем сервере у Вас больше чем 1 аккаунт, напишите никнеймы через запятую без пробела.")
            await client.send_message(channel, "Используйте команду m!commands для того что бы узнать все команды бота.")
        if channel.name == 'names':
            amount = 50
            messages = []
            async for message in client.logs_from(channel, limit=int(amount) + 1):
                messages.append(message)
            await client.delete_messages(messages)
            await client.send_message(channel, "|=====================================================================|")
            for line in file:
                await client.send_message(channel, line)
            await client.send_message(channel, "|=====================================================================|")
    file.close()


@client.command(pass_context=True)
async def info(ctx):
    channel = ctx.message.channel
    await client.send_message(channel, """Сервер для фолс программистов от тру быдлокодеров...""")

@client.command(pass_context=True)
async def lol(ctx):
    channel = ctx.message.channel
    await client.send_message(channel, "kek")

@client.command(pass_context=True)
async def commands(ctx):
    channel = ctx.message.channel
    await client.send_message(channel, """
Список команд:
m!reg nickname realname - регистрация на сервере;
m!clear count - стирание текста на сервере;
m!info - информация о сервере;
m!names - имена людей на сервере;
m!commands - команды на сервере.
""")


@client.command(pass_context=True)
async def reg(ctx, nickname, realname):
    channel = ctx.message.channel
    nickname = str(nickname)
    realname = str(realname)
    msg = "\n" + nickname + "-" + realname
    if(len(msg) > 20):
        await client.send_message(channel, "Слишком большие входные данные!")
    else:
        with open("DiscordServerNames.txt", 'a') as file:
            file.writelines(msg)
        await client.send_message(channel, "Спасибо за регистрацию!")
        file.close()


@client.command(pass_context=True)
async def names(ctx):
    file = open("DiscordServerNames.txt", "r+")
    channel = ctx.message.channel
    for line in file:
        await client.send_message(channel, line)
    file.close()


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    if(amount >= 2):
        messages = []
        async for message in client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await client.delete_messages(messages)
    else:
        await client.send_message(channel, "Введите значение которое равно или больше 2!")

client.run(token)
print('stopped')
