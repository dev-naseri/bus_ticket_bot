from bus_ticket_bot.bot.handlers.base_handler import BaseHandler
from bus_ticket_bot.bot.panels.admin.user_panel import UserPanel
from bus_ticket_bot.services.users_service import UsersService
from bus_ticket_bot.utils.logger import Logger


class BuyTicketsHandler(BaseHandler):

    @classmethod
    def register(cls):
        cls._conn.register_message_handler(
            cls.buy_tickets_handler,
            func=lambda msg: msg.text == "Buy Tickets" and UsersService.check_user_exist(msg.from_user.id)
        )

        cls._conn.register_message_handler(
            cls.vip_ticket_handler,
            func=lambda msg: msg.text == "VIP" and UsersService.check_user_exist(msg.from_user.id)
        )

        cls._conn.register_message_handler(
            cls.normal_ticket_handler,
            func=lambda msg: msg.text == "Normal" and UsersService.check_user_exist(msg.from_user.id)
        )

        cls._conn.register_message_handler(
            cls.car_ticket_handler,
            func=lambda msg: msg.text == "Car" and UsersService.check_user_exist(msg.from_user.id)
        )

    @classmethod
    def buy_tickets_handler(cls, message):
        cls._conn.send_message(
            message.chat.id,
            "Choose Ticket Type:",
            reply_markup=UserPanel.ticket_type()
        )

    @classmethod
    def vip_ticket_handler(cls, message):
        cls._conn.send_message(
            message.chat.id,
            "Please choose a date:",
            reply_markup=UserPanel.get_tickets_with_type("VIP")
        )

    @classmethod
    def normal_ticket_handler(cls, message):
        cls._conn.send_message(
            message.chat.id,
            "Please choose a date:",
            reply_markup=UserPanel.get_tickets_with_type("Normal")
        )

    @classmethod
    def car_ticket_handler(cls, message):
        cls._conn.send_message(
            message.chat.id,
            "Please choose a date:",
            reply_markup=UserPanel.get_tickets_with_type("Car")
        )