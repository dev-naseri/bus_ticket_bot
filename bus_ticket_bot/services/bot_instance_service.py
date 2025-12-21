from bus_ticket_bot.services.base_service import BaseService
from bus_ticket_bot.models.bot_instance import BotInstance
from bus_ticket_bot.utils.logger import Logger


class BotInstanceService(BaseService):
    _model = BotInstance
    _service_name = "BotInstanceService"

    @classmethod
    def change_name(cls, ):
