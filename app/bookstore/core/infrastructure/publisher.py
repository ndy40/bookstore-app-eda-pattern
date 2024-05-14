from functools import singledispatch
from typing import Any

import celery
from celery.result import AsyncResult
from celery.utils.log import get_task_logger

from bookstore.core.domain.value_objects import Event, Command
from bookstore.core.infrastructure.bus.events import event_bus
from bookstore.core.infrastructure.celery import app

_logger = get_task_logger(__name__)


@singledispatch
def publish(msg: Event | Command, return_result=False) -> Any or None:
    raise NotImplementedError


@publish.register
def _publish_event(msg: Event, return_result=False) -> Any or None:
    event_name = msg.__class__.__name__
    print("Event triggered", event_name)
    event_bus.dispatch(event_name, msg)


@publish.register
def _publish_command(msg: Command, return_result=False) -> Any or None:
    task_name = f"command.{msg.__class__.__name__.lower()}"
    result: AsyncResult = app.send_task(
        task_name,
        task_id=msg.id.hex,
        args=(msg,),
        routing_key=task_name,
    )
    _logger.info(f"Command {task_name} published")
    if return_result:
        try:
            return result.get(timeout=2)
        except celery.exceptions.TimeoutError:
            _logger.error(f"Command {task_name} failed to return result")
        finally:
            result.forget()
