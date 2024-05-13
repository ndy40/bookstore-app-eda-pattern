from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Generic, TypeVar, Dict, List, Type

from bookstore.core.domain.value_objects import Event
from bookstore.core.infrastructure.bus.utils import get_message_cls

TEvent = TypeVar("TEvent", bound=Event)


class EventHandler(ABC, Generic[TEvent]):

    @abstractmethod
    def handle(self, event: TEvent) -> None:
        pass


class EventBus:

    def __init__(self) -> None:
        self._handlers: Dict[Type[Event], List[EventHandler]] = defaultdict(list)

    def register(self, handler: EventHandler) -> None:
        self._handlers[get_message_cls(type(handler), Event)].append(handler)

    def publish(self, event: Event) -> None:
        for handler in self._handlers[type(event)]:
            self.handle(event=event, handler=handler)

    def handle(self, event: Event, handler: EventHandler) -> None:
        handler.handle(event)
