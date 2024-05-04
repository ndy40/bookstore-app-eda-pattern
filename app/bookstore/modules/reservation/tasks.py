from celery.utils.log import get_task_logger

from bookstore.core.infrastructure.bus import event_bus
from bookstore.core.infrastructure.celery import app

_logger = get_task_logger(__name__)


@event_bus.on("BookCreated")
@app.task(
    name="command.reservebook",
)
def log_book_created(msg: "BookCreated"):
    _logger.info("book was created and logged")
