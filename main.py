from bot_logic import *
import discord
import asyncio

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

#Запуск бота
@client.event
async def on_ready():
    print(f"I'm logged as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #команды
    if message.content.startswith("!hello") or message.content.startswith("!hi") or message.content.startswith("!привет"):
        await message.channel.send("Здорова чел! 👋")
    elif message.content.startswith('!bye') or message.content.startswith("!пока"):
        await message.channel.send("Ладно, пока")
    elif message.content.startswith('!pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('!smile'):
        await message.channel.send(gen_emodji())
    if message.content.startswith("!help"):
        await message.channel.send(get_help())
    elif message.content.startswith('!magic') or message.content.startswith('!магия'):
        if len(message.content) > len("!magic") and message.content.endswith('?'):
            await message.channel.send(magic_ball())
        else:
            await message.channel.send("Извините, но нету вопроса ☹️")
    #чшшш...
    elif 'Время замутить перекусончик 😎' in message.content:
        await asyncio.sleep(3)
        await message.channel.send('у меня тут в нычке 🧺')
        await asyncio.sleep(1.3)
        await message.channel.send('Вареные яички 🥚')
        await asyncio.sleep(1.85)
        await message.channel.send('Хлебушек 🍞')
        await asyncio.sleep(0.75)
        await message.channel.send('Консервы 🥫')
        await asyncio.sleep(0.8)
        await message.channel.send('и конечно кура-гриль 🍗')
        await asyncio.sleep(1.6)
        await message.channel.send('Маслята и лисички 🍄')
        await asyncio.sleep(1.75)
        await message.channel.send('Килограмм клубнички 🍓')
        await asyncio.sleep(1.65)
        await message.channel.send('Сосиски колбаса 🥩')
        await asyncio.sleep(1.4)
        await message.channel.send('и минералочки бутыль 💦')
    #else:
        #await message.channel.send(message.content)

client.run("Paste your token")
