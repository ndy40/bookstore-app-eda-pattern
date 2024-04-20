import datetime
from dataclasses import field
from typing import TypeVar, Generic

from bookstore.core.domain.value_objects import EntityUUID, Event

EntityId = TypeVar('EntityId', bound=EntityUUID)


class Entity(Generic[EntityId]):
    id: EntityId = field(hash=True)

    @classmethod
    def next_id(cls) -> EntityId:
        return EntityUUID.next_id()


class AggregateRoot(Generic[EntityId]):
    events: list[Event] = field(default_factory=list)

    def register_event(self, event: Event):
        self.events.append(event)

    def collect_event(self):
        events = self.events
        self.events = []
        return events

