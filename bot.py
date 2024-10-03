from telegram import Bot
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
key = os.getenv('API_KEY')


chat_id ='xd'


bot = Bot(token=key)

bot.send_message(chat_id=chat_id, text='siema')

# async def get_chat_id():
#     updates = await bot.get_updates()
#     for update in updates:
#         print(update.message.chat_id)
        
# if __name__ == '__main__':
#     asyncio.run(get_chat_id())