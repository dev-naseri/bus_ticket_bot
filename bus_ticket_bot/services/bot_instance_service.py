from bus_ticket_bot.services.base_service import BaseService
from bus_ticket_bot.models.bot_instance import BotInstance
from bus_ticket_bot.utils.logger import Logger


class BotInstanceData:
    def __init__(
            self, company_name, address, call, terminal_name, city_name, start_msg, help_msg,
            contactus_msg, payment_msg, refund_msg
        ):
        self.company_name = company_name
        self.address = address
        self.call = call
        self.terminal_name = terminal_name
        self.city_name = city_name
        self.start_message = start_msg
        self.help_message = help_msg
        self.contactus_message = contactus_msg
        self.payment_message = payment_msg
        self.refund_message = refund_msg


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
            data = result.data
            return BotInstanceData(
                company_name=data.company_name,
                address=data.address,
                call=data.call_number,
                terminal_name=data.terminal_name,
                city_name=data.city_name,
                start_msg=data.start_message,
                contactus_msg=data.contact_us_message,
                help_msg=data.help_message,
                payment_msg=data.payment_message,
                refund_msg=data.refund_message
            )

        Logger.service.error(
            f"Failed to fetch data from '{cls._service_name} Model'."
        )
        return result.status