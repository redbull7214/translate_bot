import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

token = str(os.getenv("API_TOKEN"))

bot = Bot(token=token)
dp = Dispatcher(bot)
