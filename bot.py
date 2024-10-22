from telegram import Bot
from dotenv import load_dotenv
import os
from telegram.error import TelegramError
#import asyncio
#import telebot
#from telebot.async_telebot import AsyncTeleBot

load_dotenv()
key = os.getenv('API_KEY')

bot = Bot(key)

async def notify_about_the_price(message):
    try:
        await bot.send_message(chat_id=903485794, text=message)
        print("Message sent successfully.")
    except TelegramError as e:
        print(f"Failed to send message: {e}")



#THIS PART IS FOR HANDLING COMMANDS, 
# MAYBE RUN ON ANOTHER THREAD OR STH, ANYWAYS IT'S RUNNING CONSTANTLY

# Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# async def send_welcome(message):
#     text = 'Hello, I will tell you the price of your product!'
#     await bot.reply_to(message, text)
    
    
# @bot.message_handler(commands=['hej'])
# async def hihi(message):
#     text = 'Hej Liv'
#     await bot.reply_to(message, text)


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# async def echo_message(message):
#     await bot.reply_to(message, str(f'{current_price} zł'))

# asyncio.run(bot.polling())
