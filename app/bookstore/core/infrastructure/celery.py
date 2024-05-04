from celery import Celery
from kombu import Queue

from bookstore.core.infrastructure.config import config


def route_queue(name, args, kwargs, options, task=None, **kw):
    queue = "celery"
    if "command" in name:
        queue = "command"
    if "event" in name:
        queue = "event"

    return {"queue": queue}


app = Celery("app", broker=config.BROKER_URL)

app.autodiscover_tasks(config.task_modules)

app.conf.result_backend = config.CELERY_RESULT_BACKEND
app.conf.task_routes = (route_queue,)
app.conf.task_eager_propagates = True
app.conf.worker_send_task_events = True
app.conf.task_send_sent_event = True
app.conf.task_serializer = "pickle"
app.conf.result_serializer = "pickle"
app.conf.task_routes = (route_queue,)
app.conf.accept_content = ["application/json", "application/x-python-serialize"]


app.conf.task_queues = (
    Queue("celery"),
    Queue(
        "command",
        routing_key="command.#",
    ),
    Queue("event", routing_key="event.#"),
)

if __name__ == "__main__":
    app.start()
