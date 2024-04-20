from typing import List

from bookstore.core.domain.value_objects import Event


class DomainEvent(Event):

    def __next__(self):
        yield self


class MultiDomainEvent(DomainEvent):
    events: List[DomainEvent]

    def __next__(self):
        yield from self.events
