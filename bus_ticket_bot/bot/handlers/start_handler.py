from bus_ticket_bot.bot.handlers.base_handler import BaseHandler
from bus_ticket_bot.bot.panels.admin.user_panel import UserPanel
from bus_ticket_bot.services.bot_instance_service import BotInstanceService
from bus_ticket_bot.services.users_service import UsersService
from bus_ticket_bot.utils.logger import Logger


class StartHandler(BaseHandler):

    @classmethod
    def register(cls):
        cls._conn.register_message_handler(
            cls.start_handler, commands=["start"]
        )

    @classmethod
    def start_handler(cls, message):
        check_user_exist = UsersService.check_user_exist(message.from_user.id)
        if not check_user_exist:
            create_user = UsersService.create_user(message.from_user.id,
                                                   message.from_user.first_name)
            if not create_user.success:
                Logger.bot.error(
                    f"Start failed because {message.from_user.id} was not create a new user."
                )
                return

        msg = BotInstanceService.get_data().start_message

        cls._conn.send_message(
            message.chat.id,
            msg,
            reply_markup=UserPanel.main_panel()
        )
