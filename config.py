import os

import telebot
from dotenv import load_dotenv

load_dotenv()

host_stage = os.getenv("URL_STAGE")
host_stage_second = os.getenv("URL_STAGE_SECOND")
host_prod = os.getenv("URL_PROD")
pol_url = os.getenv("POL_PROD_URL")
mol_url = os.getenv("MOL_PROD_URL")
review_url = os.getenv("REVIEW_URL")
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))