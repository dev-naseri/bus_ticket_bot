from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from bus_ticket_bot.bot.utils.bot_connection import BotConnection
from bus_ticket_bot.services.ticket_service import TicketsService


class UserPanel:
    _conn = BotConnection.get_bot()

    @classmethod
    def main_panel(cls):
        markup = ReplyKeyboardMarkup(row_width=1)

        buy_ticket_btn = KeyboardButton("Buy Tickets")
        your_ticket_btn = KeyboardButton("Your Tickets")
        contact_us_btn = KeyboardButton("Contact Us")

        markup.add(buy_ticket_btn, your_ticket_btn, contact_us_btn)

        return markup

    @classmethod
    def ticket_type(cls):
        markup = ReplyKeyboardMarkup(row_width=1)

        markup.add("VIP", "Normal", "Car")

        return markup

    @classmethod
    def get_tickets_with_type(cls, ticket_type):
        markup = InlineKeyboardMarkup(row_width=1)

        tickets = TicketsService.get_all_ticket(where={"ticket_type": ticket_type})

        for ticket in tickets:
            btn = InlineKeyboardButton(
                    f"{ticket.id}) {ticket.origin_city} to {ticket.city} : {ticket.price}",
                    callback_data="btn_1"
                )
            markup.add(btn)

        return markup
