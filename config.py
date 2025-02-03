import os

import telebot
from dotenv import load_dotenv

load_dotenv()

host_stage = os.getenv("URL_STAGE")
pol_url = os.getenv("POL_PROD_URL")
mol_url = os.getenv("MOL_PROD_URL")

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))