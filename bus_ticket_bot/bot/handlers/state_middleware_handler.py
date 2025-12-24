from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from bus_ticket_bot.bot.handlers.base_handler import BaseHandler
from bus_ticket_bot.bot.utils.bot_connection import BotConnection
from bus_ticket_bot.services.users_service import UsersService


class StateMiddlewareHandler(BaseHandler):

    @classmethod
    def register(cls):
        cls._conn.register_middleware_handler(
            state_handler,
            func=lambda msg: msg.text == True
        )

    @classmethod
    def state_handler(cls, message):
        user_state = UsersService.check_user_state(message.from_user.id)

        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton(
                "Exit Transaction",
                callback_data="exit_transaction"
            )
        )

        if user_state == "Transaction":
            cls._conn.send_message(
                "You have an open transaction, do you want to exit that transaction?",
            )
