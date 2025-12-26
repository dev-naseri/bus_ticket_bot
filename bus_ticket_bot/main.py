import os

from dotenv import load_dotenv
from telebot.asyncio_handler_backends import CancelUpdate

from bus_ticket_bot.bot.handlers.buy_tickets_handler import BuyTicketsHandler
from bus_ticket_bot.bot.handlers.contact_us_handler import ContactUsHandler
from bus_ticket_bot.bot.handlers.help_handler import HelpHandler
from bus_ticket_bot.bot.handlers.start_handler import StartHandler


from telebot import apihelper, TeleBot
load_dotenv()
token = os.getenv("API_TOKEN")


# StartHandler.register()
# HelpHandler.register()
# ContactUsHandler.register()
# BuyTicketsHandler.register()




blacklist= [8288322669]
open_transaction = "call_number"


def access_control(func):
    """
    if user banned don't allow to continue
    """
    def wrapper(message, *args, **kwargs):
        if message.from_user.id in blacklist:
            bot.send_message(
                message.chat.id,
                "you are banned"
            )
            return
        return func(message, *args, **kwargs)
    return wrapper


def validate_inputs(func):
    def wrapper(message, *args, **kwargs):
        if open_transaction == "call_number":
            if not message.text.isdigit() or not len(message.text) == 10:
                bot.send_message(
                    message.chat.id,
                    "Your input most be an integer in 10 length exactly.",
                )
                return
        return func(message, *args, **kwargs)
    return wrapper




@bot.message_handler(commands=['start'])
@access_control
def start(message):
    bot.send_message(
        message.chat.id,
        "Start msg"
    )

@bot.message_handler(func=lambda msg: True)
@access_control
@validate_inputs
def txt(message):
    bot.send_message(
        message.chat.id,
        "test"
    )











@bot.middleware_handler(update_types=["message"])
def middleware(instance ,message):
    # Get user_state here

    # Make sure you get the right one

    # if state == "open_transaction" and open_transaction == [any of transactions state]:
        # Get transaction_state like name, number, national_id,
            # Each this commands expect a valid data: like str, int(len(11-1))
            # so we understand that transaction have it state as well

    if message:
        # Check user is not banned return if banned

        # Check user_state change behavior on that
            # if state == "open_transaction": do not pursue and tell them you on transaction

            # if state == "Inactive"


        bot.register_message_handler(
            text,
            content_types=["text"],
            func=lambda msg: msg.text == "try it"
        )
        return

    bot.register_message_handler(
        another_type,
        content_types=["photo", "sticker"]
    )



def text(message):
    bot.send_message(
        message.chat.id,
        "test this handler"
    )

def another_type(message):
    bot.send_message(
        message.chat.id,
        "This is not a valid input"
    )

bot.infinity_polling()
