import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()


class BotConnection:
    __token = os.getenv("API_TOKEN")
    __bot = None

    @classmethod
    def get_bot(cls):
        if cls.__bot is None:
            cls.__bot = TeleBot(cls.__token)

        return cls.__bot
