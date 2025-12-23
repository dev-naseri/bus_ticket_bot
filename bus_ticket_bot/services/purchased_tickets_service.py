from random import randint

from bus_ticket_bot.models.purchased_tickets import PurchasedTickets
from bus_ticket_bot.services.base_service import BaseService
from bus_ticket_bot.utils.logger import Logger


class PurchasedTicketsService(BaseService):
    _model = PurchasedTickets
    _service_name = "PurchasedTicketsService"

    @classmethod
    def _generate_transaction_code(cls, user_id, length=8):
        """
        Generate a numeric unique code based on user_id and random digits
        """
        random_part = randint(10**(length-1), 10**length - 1)
        all_code = int(f"{user_id}{random_part}")

        return all_code

    @classmethod
    def add_purchase(cls, telegram_id, ticket_id, user_id, receipt):
        result = cls.create(
            telegram_id=telegram_id, ticket_id=ticket_id, user_id=user_id,
            transaction_id=cls._generate_transaction_code(user_id),
            active=False, receipt=receipt
        )

        if result.success:
            Logger.service.info(
                f"User: {user_id} successfully purchased ticket: {ticket_id}."
            )
            return result.status
        Logger.service.error(
            f"User failed to purchase ticket."
        )
        return result.status

    @classmethod
    def activate_purchase(cls, transaction_id):
        result = cls.update(
            find_by={"transaction_id": transaction_id},
            update_data={"active": True}
        )

        if result.success:
            Logger.service.info(
                f"Successfully activated '{transaction_id}' on "
                f"'{cls._service_name} Model'."
            )
            return result.status
        Logger.service.error(
            f"Failed to activate user ticket '{cls._service_name} Model'."
        )
        return result.status

    @classmethod
    def deactivate_ticket(cls, transaction_id):
        result = cls.delete(transaction_id=transaction_id)

        if result.success:
            Logger.service.info(
                f"Successfully deleted '{transaction_id}' from "
                f"'{cls._service_name} Model'."
            )
            return result.status
        Logger.service.error(
            f"Failed to delete ticket from '{cls._service_name} Model'."
        )
        return result.status
