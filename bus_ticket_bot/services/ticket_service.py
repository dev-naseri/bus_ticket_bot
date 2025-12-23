from datetime import datetime, timedelta

import khayyam
from khayyam import JalaliDatetime

from bus_ticket_bot.services.base_service import BaseService
from bus_ticket_bot.models.tickets import Tickets
from bus_ticket_bot.utils.logger import Logger


class TicketsService(BaseService):
    _model = Tickets
    _service_name = "TicketService"

    @classmethod
    def add_special_ticket(cls, name, city, date, price,
                       destination_terminal=None, ticket_type="VIP"):
        if ticket_type not in ["VIP", "Normal", "Car"]:
            Logger.service.error(
                f"Given ticket_type input for add_special_ticket is not valid, "
                f"it most be 'VIP', 'Normal' or 'Car'."
            )
            return "INVALID_TICKET_TYPE_INPUT"

        result = cls.create(
            full_name=name, ticket_type=ticket_type, city=city.lower(),
            destination_terminal=destination_terminal, date=date,
            price=price
        )

        if result.success:
            Logger.service.info(
                f"New Ticket to city {city} Added to the database."
            )
            return result.status
        Logger.service.error(
            f"Failed to add ticket to {city} in database."
        )
        return result.status

    @classmethod
    def add_no_pattern_ticket(
        cls, full_name, ticket_type, origin_city, origin_terminal, city,
        destination_terminal, date, price
    ):
        if ticket_type not in ["VIP", "Normal", "Car"]:
            Logger.service.error(
                f"Given ticket_type input for add_special_ticket is not valid, "
                f"it most be 'VIP', 'Normal' or 'Car'."
            )
            return "INVALID_TICKET_TYPE_INPUT"

        result = cls.create(
            full_name=full_name, origin_city=origin_city,
            origin_terminal=origin_terminal, ticket_type=ticket_type,
            city=city.lower(), destination_terminal=destination_terminal,
            date=date, price=price
        )

        if result.success:
            Logger.service.info(
                f"New Ticket to city {city} Added to the database."
            )
            return result.status
        Logger.service.error(
            f"Failed to add ticket to {city} in database."
        )
        return result.status

    @classmethod
    def get_ticket(cls, **filters):
        result = cls.select(**filters)

        if result.success:
            Logger.service.info(
                f"Successfully select ticket {result.data.id} from database."
            )
            return result.data
        Logger.service.error(
            f"Failed to fetch ticket from database."
        )
        return result.status


    @classmethod
    def get_all_ticket(cls, where=None):
        if where is None:
            seven_days_ago = datetime.now() - timedelta(days=7)
            where = {"date__gte": seven_days_ago}

        result = cls.select_all(where=where)

        if result.success:
            Logger.service.info(
                f"Successfully select_all ticket from '{cls._service_name} "
                f"Model' database."
            )
            return result.data
        Logger.service.error(
            f"Failed to fetch tickets from '{cls._service_name} Model'"
            f" database."
        )
        return result.status

    @classmethod
    def remove_ticket(cls, **filters):
        result = cls.delete(**filters)

        if result.success:
            Logger.service.info(
                f"Successfully deleted records from '{cls._service_name} Model'"
            )
            return result.status
        Logger.service.error(
            f"Failed to delete data from '{cls._service_name} Model'."
        )
        return result.status

    @classmethod
    def edit_ticket(cls, find_by, update_data):
        result = cls.update(find_by, update_data)

        if result.success:
            Logger.service.info(
                f"Successfully Updated Data on '{cls._service_name} Model'."
            )
            return result.status
        Logger.service.error(
            f"Failed to update data on '{cls._service_name} Model'."
        )
        return result.status
