from abc import ABC, abstractmethod

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from bus_ticket_bot.services.users_service import UsersService

from bus_ticket_bot.bot.utils.bot_connection import BotConnection


class BaseHandler(ABC):
    _conn = BotConnection.get_bot()

    @classmethod
    def block_if_transaction(cls, message):
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
                message.chat.id,
                "You have an open transaction, do you want to exit that transaction?",
                reply_markup=markup
            )
            return True
        return False

    @abstractmethod
    def register(self):
        pass
