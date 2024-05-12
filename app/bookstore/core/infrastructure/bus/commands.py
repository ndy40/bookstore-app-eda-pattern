from abc import ABC, abstractmethod
from types import FunctionType
from typing import TypeVar, Generic, Dict, Type, Callable

from celery.local import PromiseProxy

from bookstore.core.domain.value_objects import Command
from bookstore.core.infrastructure.bus.exceptions import (
    MissingCommandHandlerException,
)
from bookstore.core.infrastructure.bus.utils import (
    get_message_cls,
    WrongHandlerException,
)

TCommand = TypeVar("TCommand", bound=Command)


HandlerFuncType = Callable[[TCommand], None]


class CommandHandler(ABC, Generic[TCommand]):
    @abstractmethod
    def handle(self, command: TCommand) -> None:
        pass


class CommandBus:

    def __init__(self):
        self._handlers: Dict[Type[Command], CommandHandler] = {}

    def register(self, handler: CommandHandler | HandlerFuncType) -> None:
        command_cls = None
        try:
            command_cls = get_message_cls(type(handler), Command)
        except WrongHandlerException:

            if isinstance(handler, (FunctionType, PromiseProxy)):
                first_input, *_ = handler.__annotations__.items()
                command_cls = first_input[1]

        if command_cls in self._handlers:
            raise ValueError()

        if command_cls is None:
            raise ValueError("Unsupported handler")

        self._handlers[command_cls] = handler

    def execute(self, command: Command) -> None:
        try:
            self.handle(command=command, handler=self._handlers[type(command)])
        except KeyError:
            raise MissingCommandHandlerException()

    def handle(
        self, command: Command, handler: CommandHandler | HandlerFuncType | PromiseProxy
    ) -> None:
        if hasattr(handler, "handle") and callable(getattr(handler, "handle", None)):
            handler.handle(command)
        elif isinstance(handler, PromiseProxy):
            handler.delay(command)
        else:
            handler(command)


command_bus = CommandBus()
