from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class ServiceResult(Generic[T]):
    """
    Standard result object returned by service-layer operations.

    Attributes:
        success (bool): Indicates whether the operation was successful.
        data (Optional[T]): Returned data (model instance, list, etc.) if successful.
        status (str): Machine-readable status code describing the result.
    """

    success: bool
    data: Optional[T] = None
    status: str = "OK"
    message: str = ""
