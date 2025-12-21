from bus_ticket_bot.services.base_service import BaseService
from bus_ticket_bot.models.admins import Admins
from bus_ticket_bot.utils.logger import Logger


class AdminsService(BaseService):
    _model = Admins
    _service_name = "AdminService"

    @classmethod
    def create_admin(cls, telegram_id):
        if (
            not telegram_id
            or not isinstance(telegram_id, int)
        ):
            Logger.service.error(
                f"Given telegram_id input for {cls._service_name} is not valid."
            )
            return "INVALID_INPUTS"

        result = cls.create(
            telegram_id=telegram_id
        )

        Logger.service.info(
            f"create_admin action for {cls._service_name} result:"
            f" {result.message}"
        )
        return result.status

