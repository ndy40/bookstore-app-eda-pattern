from datetime import datetime

from bookstore.core.domain.value_objects import ValueObject


class Author(ValueObject):
    first_name: str
    last_name: str
    dob: datetime.date | None = None


class StatusAttribute(ValueObject):
    total_quantity: int | None = 0
    available_quantity: int | None = None
