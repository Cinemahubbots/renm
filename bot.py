from pyrogram import Client
from config import *
from route import web_server
from aiohttp import web

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "main"},
            sleep_threshold=10,
        )


bot = Bot()
bot.run()
