from celery.utils.log import get_task_logger

from bookstore.core.infrastructure.celery import app

_logger = get_task_logger(__name__)


@app.task(
    name="command.reservebook",
)
def log_book_created(msg: "ReserveBook"):
    _logger.info("book was created and logged")
