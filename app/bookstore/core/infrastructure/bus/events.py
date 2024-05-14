from collections import defaultdict
from functools import wraps
from typing import Callable

from bookstore.core.domain.constants import EventRegistry
from bookstore.core.infrastructure.celery import app


class EventBus:
    """Simple eventbus for registering callables interested in an event"""

    _events = defaultdict(set)

    @classmethod
    def on(cls, event: str):
        def outer(func):
            cls.add_event(func, event)

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return outer

    @classmethod
    def add_event(cls, func: Callable, event: EventRegistry):
        cls._events[event].add(func.name)

    @staticmethod
    def dispatch(event: str, *args, **kwargs):
        if event in EventBus._events:
            for task_name in EventBus._events[event]:
                payload = {}
                if args:
                    payload["args"] = tuple(args)
                else:
                    payload["kwarg"] = kwargs

                app.send_task(task_name, routing_key=task_name, **payload)

    @classmethod
    def clear(cls, event):
        if event in EventBus._events:
            del cls._events[event]

    @classmethod
    def events(cls):
        return cls._events


event_bus = EventBus
