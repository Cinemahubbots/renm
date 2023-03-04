from pyrogram import Client
from config import *
import time
import os

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

STRING = os.environ.get("STRING", "")

app = Client("prmium", api_id=API_ID, api_hash=API_HASH, session_string=STRING)

bot = Bot()
bot.run()
app.start()
