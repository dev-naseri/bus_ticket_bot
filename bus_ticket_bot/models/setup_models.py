from bus_ticket_bot.models.db_settings import db
from bus_ticket_bot.utils.logger import Logger


def create_db_tables():
    from bus_ticket_bot.models.admins import Admins
    from bus_ticket_bot.models.bot_instance import BotInstance
    from bus_ticket_bot.models.users import Users
    from bus_ticket_bot.models.tickets import Tickets
    from bus_ticket_bot.models.purchased_tickets import PurchasedTickets
    from bus_ticket_bot.models.refound_requests import RefoundRequests

    try:
        db.create_tables(
            [Admins, BotInstance, Users, Tickets, PurchasedTickets,
             RefoundRequests]
        )
        Logger.service.info("Creating database models was Successful.")
        return True
    except Exception as e:
        db.rollback()
        Logger.service.error(f"Failed to create database models because: {e}")
        return False