from telegram import Bot
from dotenv import load_dotenv
import os
import asyncio
import telebot
from main import current_price

load_dotenv()
key = os.getenv('API_KEY')


from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(key)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hello, I will tell you the price of your product!'
    await bot.reply_to(message, text)
    
    
@bot.message_handler(commands=['hej'])
async def hihi(message):
    text = 'Hej Liv'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, str(f'{current_price} zł'))


# async def notify_about_the_price(price):
#     await bot.send_message(chat_id=903485794, text=str(f'{current_price} zł'))


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