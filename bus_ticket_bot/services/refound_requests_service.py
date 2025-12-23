from bus_ticket_bot.models.refound_requests import RefoundRequests
from bus_ticket_bot.services.base_service import BaseService
from bus_ticket_bot.utils.logger import Logger


class RefoundRequestsService(BaseService):
    _model = RefoundRequests
    _service_name = "RefoundRequestsService"

    @classmethod
    def add_refound_request(
        cls, transaction_id, telegram_id: int, receipt_id: str, refound_request_id: str, reason: str=""
    ):
        result = cls.create(
            transaction_id=transaction_id, telegram_id=telegram_id, receipt_id=receipt_id,
            refound_request_id=refound_request_id, reason=reason
        )

        if result.success:
            Logger.service.info(
                f"Successfully added New refound request added to '{cls._service_name} Model'."
            )
            return result.status
        Logger.service.error(
            f"Failed to add Refound Request to '{cls._service_name} Model'."
        )
        return result.status

    @classmethod
    def get_refound_request(cls, transaction_id):
        result = cls.select(transaction_id=transaction_id)

        if result.success:
            Logger.service.info(
                f"Successfully selected '{result.id}' from '{cls._service_name} Model'."
            )
            return result.data
        Logger.service.error(
            f"Failed to select refound request from database because: '{result.message}'."
        )
        return result.status

    @classmethod
    def delete_refound_request(cls, transaction_id):
        result = cls.delete(transaction_id=transaction_id)

        if result.success:
            Logger.service.info(
                f"Successfully deleted '{result.id}' from '{cls._service_name} Model'."
            )
            return result.status
        Logger.service.error(
            f"Failed to delete refound request from '{cls._service_name} Model' because: "
            f"{result.message}"
        )
        return result.status
