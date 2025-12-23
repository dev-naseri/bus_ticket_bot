from bus_ticket_bot.bot.handlers.base_handler import BaseHandler
from bus_ticket_bot.services.bot_instance_service import BotInstanceService


class HelpHandler(BaseHandler):

    @classmethod
    def register(cls):
        cls._conn.register_message_handler(
            cls.help_handler, commands=['help']
        )

    @classmethod
    def help_handler(cls, message):
        msg = BotInstanceService.get_data().help_message

        cls._conn.send_message(
            message.chat.id,
            msg
        )
