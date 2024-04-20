from functools import singledispatch

from bookstore.core.domain.value_objects import Event, Command


@singledispatch
def publish(msg: Event | Command):
    raise NotImplemented


@publish.register
def publish_event(msg: Event):
    print("Firing event")


@publish.register
def publish_command(msg: Command):
    print('firing commands')

