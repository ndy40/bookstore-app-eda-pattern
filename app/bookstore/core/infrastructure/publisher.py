from functools import singledispatch

from celery.utils.log import get_task_logger

from bookstore.core.domain.value_objects import Event, Command
from bookstore.core.infrastructure.celery import app

_logger = get_task_logger(__name__)


@singledispatch
def publish(msg: Event | Command):
    raise NotImplemented


def _publish_event(msg: Event):
    task_name = f"event.{msg.__class__.__name__.lower()}"
    app.send_task(
        task_name,
        task_id=msg.id.hex,
        args=(msg,),
        routing_key=task_name,
    )
    _logger.info(f"Event {task_name} published")


def _publish_command(msg: Command):
    task_name = f"command.{msg.__class__.__name__.lower()}"
    app.send_task(
        task_name,
        task_id=msg.id.hex,
        args=(msg,),
        routing_key=task_name,
    )

    _logger.info(f"Command {task_name} published")


@publish.register
def publish_lists(*messages: Command | Event):
    for msg in messages:
        if isinstance(msg, Command):
            _publish_command(msg)
        else:
            _publish_event(msg)
