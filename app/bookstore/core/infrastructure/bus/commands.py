from abc import ABC, abstractmethod
from types import FunctionType
from typing import TypeVar, Generic, Dict, Type, Callable, Any

from celery.local import PromiseProxy
from celery.result import AsyncResult

from bookstore.core.domain.value_objects import Command
from bookstore.core.infrastructure.bus.exceptions import (
    MissingCommandHandlerException, CommandHandlerRegisteredException,
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
            raise CommandHandlerRegisteredException()

        if command_cls is None:
            raise ValueError("Unsupported handler")

        self._handlers[command_cls] = handler

    def execute(self, command: Command) -> Any | None:
        try:
            return self.handle(command=command, handler=self._handlers[type(command)])
        except KeyError:
            raise MissingCommandHandlerException()

    def handle(
            self, command: Command, handler: CommandHandler | HandlerFuncType | PromiseProxy
    ) -> None:
        result = None
        if hasattr(handler, "handle") and callable(getattr(handler, "handle", None)):
            return handler.handle(command)
        elif isinstance(handler, PromiseProxy):
            task_result: AsyncResult = handler.delay(command)
            result = task_result.get(timeout=20)
        else:
            result = handler(command)

        return result


command_bus = CommandBus()
