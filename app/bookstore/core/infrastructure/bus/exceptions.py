class CommandBusException(Exception):
    pass


class MissingCommandHandlerException(CommandBusException):
    pass


class CommandHandlerRegisteredException(CommandBusException):
    pass
