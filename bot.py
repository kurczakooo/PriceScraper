from telegram import Bot
from dotenv import load_dotenv
import os
import asyncio
import telebot

load_dotenv()
key = os.getenv('API_KEY')


from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(key)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    #await bot.reply_to(message, 'chuj')
    await bot.send_message(chat_id=903485794, text='aha xd')



asyncio.run(bot.polling())









# chat_id = '@pkurczakooo'
# bot = Bot(token=key)

# async def notify(message):
#     await bot.send_message(chat_id=chat_id, text=message)

# async def get_chat_id():
#     updates = await bot.get_updates()
#     print("Updates received:", updates)
#     for update in updates:
#         print(update.message.chat_id)
        
# if __name__ == '__bot__':
#     asyncio.run(notify('xdddddd'))