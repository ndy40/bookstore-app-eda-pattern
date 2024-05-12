import dataclasses
from dataclasses import field
from typing import TypeVar, Generic

from bunnet import PydanticObjectId

from bookstore.core.domain.value_objects import EntityUUID, Event

EntityId = TypeVar("EntityId", bound=EntityUUID)


@dataclasses.dataclass
class Entity(Generic[EntityId]):
    id: EntityId = field(hash=True, default_factory=PydanticObjectId)


class AggregateRoot(Entity[EntityId]):
    events: list[Event] = field(default_factory=list)

    def register_event(self, event: Event):
        self.events.append(event)

    def collect_event(self):
        events = self.events
        self.events = []
        return events
