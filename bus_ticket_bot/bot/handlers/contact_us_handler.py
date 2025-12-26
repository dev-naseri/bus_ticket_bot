from bus_ticket_bot.bot.handlers.base_handler import BaseHandler
from bus_ticket_bot.services.bot_instance_service import BotInstanceService


class ContactUsHandler(BaseHandler):

    @classmethod
    def register(cls):
        cls._conn.register_message_handler(
            cls.contact_us_handler, commands=['contactus']
        )

    @classmethod
    def contact_us_handler(cls, message):
        if cls.block_if_transaction(message):
            return

        msg = BotInstanceService.get_data().contact_us_message

        cls._conn.send_message(
            message.chat.id,
            msg
        )
