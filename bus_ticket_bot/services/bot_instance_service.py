from bus_ticket_bot.services.base_service import BaseService
from bus_ticket_bot.models.bot_instance import BotInstance
from bus_ticket_bot.utils.logger import Logger


class BotInstanceService(BaseService):
    _model = BotInstance
    _service_name = "BotInstanceService"

    @classmethod
    def change_field(cls, **kwargs):
        # Validate Field
        if 1 < len(kwargs) < 1:
            Logger.service.error(
                f"change_filed in {cls._service_name} only get one argument not "
                f"more."
            )
            return "MORE_THAN_ONE_ARGUMENT_ERROR"

        for key, value in kwargs.items():
            result = cls.update(
                find_by={"id": 1},
                update_data={key: value}
            )

        if result.success:
            Logger.service.error(
                f"Successfully changed '{kwargs}' in '{cls._service_name} "
                f"Model'."
            )
            return result.status
        Logger.service.error(
            f"Failed to change '{kwargs}' in '{cls._service_name} Model'."
        )
        return False

    @classmethod
    def get_data(cls):
        result = cls.select(id=1)

        if result.success:
            Logger.service.info(
                f"Data from '{cls._service_name} Model' fetched successfully."
            )
            return result.data

        Logger.service.error(
            f"Failed to fetch data from '{cls._service_name} Model'."
        )
        return result.status