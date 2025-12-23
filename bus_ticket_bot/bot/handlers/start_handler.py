from bus_ticket_bot.bot.handlers.base_handler import BaseHandler
from bus_ticket_bot.services.bot_instance_service import BotInstanceService


class StartHandler(BaseHandler):

    @classmethod
    def register(cls):
        cls._conn.register_message_handler(
            cls.start_handler, commands=["start"]
        )

    @classmethod
    def start_handler(cls, message):
        msg = BotInstanceService.get_data().start_message

        cls._conn.send_message(
            message.chat.id,
            msg
        )
