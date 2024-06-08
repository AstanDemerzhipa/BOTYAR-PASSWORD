import discord
from bot_logic import gen_pass
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$Как дела?'):
        await message.channel.send("Как ты?")
    else:
        await message.channel.send("Твой пароль" + gen_pass(10) )

client.run("MTI0OTAyNTI1MzcwMzk0NjI5MA.Gmwr2l.sHbZA7aeI7h7DtBlIvkP7mOooxQigJ756HzJMA")
