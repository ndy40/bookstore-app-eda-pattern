from uuid import UUID, uuid4

from bunnet import PydanticObjectId
from pydantic import BaseModel, Field, ConfigDict


class EntityUUID(PydanticObjectId): ...


class Message(BaseModel):
    id: UUID | None = Field(default_factory=uuid4, alias="_id")

    model_config = ConfigDict(frozen=True)

    def get_alias(self):
        return self.__class__


class Event(Message):
    # base class for all events
    ...


class Command(Message):
    # base class for all commands.
    ...


class ValueObject:
    # base value object
    ...
