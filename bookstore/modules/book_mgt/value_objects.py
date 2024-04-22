import dataclasses
import datetime
from typing import Optional

from bookstore.core.domain.value_objects import ValueObject


class Name(str):
    def __new__(cls, name):
        return super().__new__(cls, name.strip())


@dataclasses.dataclass
class Author(ValueObject):
    first_name: Name
    last_name: Name
    dob: Optional[datetime.date] = None


@dataclasses.dataclass
class StatusAttribute(ValueObject):
    total_quantity: int | None = 0
    available_quantity: int | None = None
