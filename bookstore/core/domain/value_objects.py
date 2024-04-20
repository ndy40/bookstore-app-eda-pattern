import dataclasses
from dataclasses import field
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class EntityUUID(UUID):
    @classmethod
    def next_id(cls):
        return cls(hex=uuid4().hex)


class Message(BaseModel):
    id: UUID | None = Field(default_factory=uuid4, alias='_id')

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

