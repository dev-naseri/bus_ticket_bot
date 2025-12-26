"""

Check User Warnings:
    if user_warnings >= 3:
        send_message( You are banned )
        return
    else:
        let it pass

Check User State:
    if user have open_transactions:
        step = get_transaction_step()
        if input is not valid and match with step:
            send_message( your value is not valid for this step it should be integer (perhaps) )
            return
        else:
            do nothing let it pass (run)


"""
from telebot.apihelper import send_message

from bus_ticket_bot.bot.utils.bot_connection import BotConnection
from bus_ticket_bot.main import open_transaction
from bus_ticket_bot.services.users_service import UsersService


class UserAuthentication:
    _conn = BotConnection.get_bot()

    def __init__(self, func):
        self.func = func

    def __call__(self, message, *args, **kwargs):
        user = UsersService.get_user(message.from_user.id)

        if isinstance(user, str):
            return

        is_user_banned = self.check_warnings(user.warnings)
        open_transaction = user.open_transaction

        if is_user_banned:
            return

        if open_transaction != "empty":
            if open_transaction == "full_name":
                valid = self.validate_input()
                if not valid:
                    self._conn.send_message(
                        ""
                    )

    @staticmethod
    def check_warnings(warnings):
        """
        if warning >= 3: User Banned
        else: User OK
        """
        if not isinstance(warnings, int):
            return "INVALID_INPUT"

        if warnings >= 3:
            return True
        return False

    @staticmethod
    def get_transaction_step():
