from bus_ticket_bot.models.users import Users
from bus_ticket_bot.services.base_service import BaseService
from bus_ticket_bot.utils.logger import Logger


class UsersService(BaseService):
    _model = Users
    _service_name = "UsersService"

    @classmethod
    def create_user(cls, telegram_id, full_name=None, warnings=0):
        # Validate telegram_id
        if (
            not telegram_id
            or not isinstance(telegram_id, int)
        ):
            Logger.service.error(
                f"Given telegram_id input for {cls._service_name} is not valid."
            )
            return "INVALID_INPUTS"

        # Validate full_name
        if (
            full_name
            and not isinstance(full_name, str)
        ):
            Logger.service.error(
                f"Given full_name input for {cls._service_name} is not valid."
            )
            return "INVALID_INPUTS"


        # Validate warnings
        if (
            warnings
            and not isinstance(warnings, int)
        ):
            Logger.service.error(
                f"Given telegram_id input for {cls._service_name} is not valid."
            )
            return "INVALID_INPUTS"

        create = cls.create(
            telegram_id=telegram_id
        )

        return create

    @classmethod
    def check_warnings(cls, telegram_id):
        """
        if user warnings is more than equal or more than three return True
        :param telegram_id: int
        :return: bool (True of user has 3 or more warning else false)
        """
        if (
                not telegram_id
                or not isinstance(telegram_id, int)
        ):
            Logger.service.error(
                f"Given telegram_id input for {cls._service_name} is not valid."
            )
            return "INVALID_INPUTS"

        result = cls.select(
            telegram_id=telegram_id
        )

        if result.success:
            if result.data.warnings >= 3:
                Logger.service.info(
                    f"User: {telegram_id} is banned."
                )
                return True

            Logger.service.warning(
                f"User: {telegram_id} is not banned."
            )
            return False

        Logger.service.error(
            f"User: {telegram_id} check_warnings failed because: "
            f"{result.message}"
        )
        return result.status

    @classmethod
    def add_user_warnings(cls, telegram_id):
        if (
            not telegram_id
            or not isinstance(telegram_id, int)
        ):
            Logger.service.error(
                f"Given telegram_id input for {cls._service_name} is not valid."
            )
            return "INVALID_INPUTS"

        result = cls.select(telegram_id=telegram_id)

        if result.success:
            if not result.data.warnings >= 3:
                result.data.warnings += 1
                result.data.save()
                Logger.service.info(
                    f"Add warning to {telegram_id} Account was successful."
                )
                return result.status
            elif result.data.warnings >= 3:
                Logger.service.warning(
                    f"User {telegram_id} has reach warnings limit. this account"
                    f" is banned from our telegram bot."
                )
                return "USER_BANNED"

        Logger.service.error(
            f"Adding Warning for account: {telegram_id} failed because: "
            f"{result.message}."
        )
        return result.status
