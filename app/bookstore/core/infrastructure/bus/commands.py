from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Type

from bookstore.core.domain.value_objects import Command
from bookstore.core.infrastructure.bus.exceptions import (
    CommandHandlerRegisteredException,
    MissingCommandHandlerException,
)
from bookstore.core.infrastructure.bus.utils import get_message_cls

TCommand = TypeVar("TCommand", bound=Command)


class CommandHandler(ABC, Generic[TCommand]):
    @abstractmethod
    def handle(self, command: TCommand) -> None:
        pass


class CommandBus:

    def __init__(self):
        self._handlers: Dict[Type[Command], CommandHandler] = {}

    def register(self, handler: CommandHandler) -> None:
        command_cls = get_message_cls(type(handler), Command)
        if command_cls in self._handlers:
            raise CommandHandlerRegisteredException()
        self._handlers[command_cls] = handler

    def execute(self, command: Command) -> None:
        try:
            self.handle(command=command, handler=self._handlers[type(command)])
        except KeyError:
            raise MissingCommandHandlerException()

    def handle(self, command: Command, handler: CommandHandler) -> None:
        handler.handle(command)
