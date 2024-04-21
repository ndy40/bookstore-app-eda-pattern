from datetime import datetime
from typing import Optional

from bookstore.core.domain.value_objects import ValueObject


class Author(ValueObject):
    first_name: str
    last_name: str
    dob: Optional[datetime.date] = None


class StatusAttribute(ValueObject):
    total_quantity: int | None = 0
    available_quantity: int | None = None
