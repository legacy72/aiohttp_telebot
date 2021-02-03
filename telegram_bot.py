import base64

import asyncio
import configparser
from telethon.sync import TelegramClient

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)

client.start()


async def ask_eye_of_god_bot(phone_number):
    chat = 'EyeGodsBot'
    await client.send_message(chat, phone_number)
    await asyncio.sleep(3)
    res = {}
    async for message in client.iter_messages(chat, limit=2):
        if message.media:
            res['photo'] = str(base64.b64encode(message.media.photo.sizes[0].bytes))
        else:
            res['text'] = message.text
    return res
