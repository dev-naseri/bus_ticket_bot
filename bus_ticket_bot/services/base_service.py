from abc import ABC
from typing import Dict, Optional, Any
from peewee import IntegrityError, OperationalError
from bus_ticket_bot.models.db_settings import db
from bus_ticket_bot.utils.logger import Logger
from bus_ticket_bot.services.status_codes import StatusCode
from bus_ticket_bot.services.service_result import ServiceResult


class BaseService(ABC):
    """
    Base CRUD service for database operations.

    This class provides low-level Create, Read, Update, and Delete operations.
    Concrete services should:
        - Set `_model`
        - Set `_service_name`
        - Add business-specific logic on top of these methods
    """

    _model = None
    _service_name = None

    # -------------------- CREATE --------------------

    @classmethod
    def create(cls, **data) -> ServiceResult:
        try:
            with db.atomic():
                instance = cls._model.create(**data)

            Logger.service.info(
                f"[{cls._service_name}] Record created successfully (ID: {instance.id})."
            )

            return ServiceResult(
                success=True,
                status=StatusCode.CREATED,
                data=instance,
                message="Record created successfully."
            )

        except IntegrityError:
            Logger.service.warning(
                f"[{cls._service_name}] Create failed: duplicate or constraint violation."
            )
            return ServiceResult(
                success=False,
                status=StatusCode.DUPLICATE_OR_INVALID,
                message="Record already exists or violates constraints."
            )

        except OperationalError as exc:
            Logger.service.critical(
                f"[{cls._service_name}] Database error during create: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.DB_ERROR,
                message="Database operational error."
            )

        except Exception as exc:
            Logger.service.error(
                f"[{cls._service_name}] Unexpected error during create: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.UNEXPECTED_ERROR,
                message=str(exc)
            )

    # -------------------- DELETE --------------------

    @classmethod
    def delete(cls, **filters) -> ServiceResult:
        try:
            query = cls._model.select()

            query = cls._apply_where(query, filters)

            instance = query.get_or_none()
            if not instance:
                Logger.service.info(
                    f"[{cls._service_name}] Delete skipped: record not found."
                )
                return ServiceResult(
                    success=False,
                    status=StatusCode.NOT_FOUND,
                    message="Record not found."
                )

            with db.atomic():
                instance.delete_instance()

            Logger.service.info(
                f"[{cls._service_name}] Record deleted (ID: {instance.id})."
            )

            return ServiceResult(
                success=True,
                status=StatusCode.DELETED,
                message="Record deleted successfully."
            )

        except OperationalError as exc:
            Logger.service.critical(
                f"[{cls._service_name}] Database error during delete: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.DB_ERROR,
                message="Database operational error."
            )

        except Exception as exc:
            Logger.service.error(
                f"[{cls._service_name}] Unexpected error during delete: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.UNEXPECTED_ERROR,
                message=str(exc)
            )

    # -------------------- SELECT ONE --------------------

    @classmethod
    def select(cls, **filters) -> ServiceResult:
        try:
            query = cls._model.select()

            query = cls._apply_where(query, filters)

            instance = query.get_or_none()
            if not instance:
                Logger.service.info(
                    f"[{cls._service_name}] Select result: record not found."
                )
                return ServiceResult(
                    success=False,
                    status=StatusCode.NOT_FOUND,
                    message="Record not found."
                )

            return ServiceResult(
                success=True,
                status=StatusCode.OK,
                data=instance,
                message="Record retrieved successfully."
            )

        except OperationalError as exc:
            Logger.service.critical(
                f"[{cls._service_name}] Database error during select: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.DB_ERROR,
                message="Database operational error."
            )

        except Exception as exc:
            Logger.service.error(
                f"[{cls._service_name}] Unexpected error during select: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.UNEXPECTED_ERROR,
                message=str(exc)
            )

    # -------------------- SELECT MANY --------------------

    @classmethod
    def select_all(
        cls,
        where: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
    ) -> ServiceResult:
        if limit is not None and not isinstance(limit, int):
            return ServiceResult(
                success=False,
                status=StatusCode.INVALID_INPUT,
                message="Limit must be an integer."
            )

        if where is not None and not isinstance(where, dict):
            return ServiceResult(
                success=False,
                status=StatusCode.INVALID_INPUT,
                message="Where must be a dictionary."
            )

        try:
            query = cls._model.select()

            if where:
                query = cls._apply_where(query, where)

            if limit:
                query = query.limit(limit)

            return ServiceResult(
                success=True,
                status=StatusCode.OK,
                data=query,
                message="Records retrieved successfully."
            )

        except OperationalError as exc:
            Logger.service.critical(
                f"[{cls._service_name}] Database error during select_all: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.DB_ERROR,
                message="Database operational error."
            )

        except Exception as exc:
            Logger.service.error(
                f"[{cls._service_name}] Unexpected error during select_all: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.UNEXPECTED_ERROR,
                message=str(exc)
            )

    # -------------------- UPDATE --------------------

    @classmethod
    def update(cls, find_by: Dict, update_data: Dict) -> ServiceResult:
        if not isinstance(find_by, dict) or not isinstance(update_data, dict):
            return ServiceResult(
                success=False,
                status=StatusCode.INVALID_INPUT,
                message="Invalid input data."
            )

        try:
            query = cls._model.select()

            query = cls._apply_where(query, find_by)

            instance = query.get_or_none()
            if not instance:
                return ServiceResult(
                    success=False,
                    status=StatusCode.NOT_FOUND,
                    message="Record not found."
                )

            # Validate update_data fields
            invalid_fields = [
                field for field in update_data
                if field not in cls._model._meta.fields
            ]
            if invalid_fields:
                Logger.service.error(
                    f"[{cls._service_name}] Invalid update fields: {invalid_fields}"
                )
                return ServiceResult(
                    success=False,
                    status=StatusCode.INVALID_FIELD,
                    message=f"Invalid update fields: {', '.join(invalid_fields)}"
                )

            with db.atomic():
                for field, value in update_data.items():
                    if field in ("id", "created_at"):
                        continue
                    setattr(instance, field, value)

                instance.save()

            return ServiceResult(
                success=True,
                status=StatusCode.UPDATED,
                data=instance,
                message="Record updated successfully."
            )

        except OperationalError as exc:
            Logger.service.critical(
                f"[{cls._service_name}] Database error during update: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.DB_ERROR,
                message="Database operational error."
            )

        except Exception as exc:
            Logger.service.error(
                f"[{cls._service_name}] Unexpected error during update: {exc}"
            )
            return ServiceResult(
                success=False,
                status=StatusCode.UNEXPECTED_ERROR,
                message=str(exc)
            )

    # -------------------- PRIVATE: APPLY WHERE --------------------

    @classmethod
    def _apply_where(cls, query, where: dict):
        """
        Apply where conditions with support for operators:
        eq, gt, gte, lt, lte using Django-style __ syntax.
        """
        for key, value in where.items():
            if "__" in key:
                field_name, operator = key.split("__", 1)
            else:
                field_name, operator = key, "eq"

            if field_name not in cls._model._meta.fields:
                raise ValueError(f"Invalid field: {field_name}")

            field = getattr(cls._model, field_name)

            if operator == "eq":
                query = query.where(field == value)
            elif operator == "gt":
                query = query.where(field > value)
            elif operator == "gte":
                query = query.where(field >= value)
            elif operator == "lt":
                query = query.where(field < value)
            elif operator == "lte":
                query = query.where(field <= value)
            else:
                raise ValueError(f"Invalid operator: {operator}")

        return query
