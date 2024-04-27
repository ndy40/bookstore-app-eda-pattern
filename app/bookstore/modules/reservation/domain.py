from bookstore.core.domain.models import AggregateRoot


class ReservedBook(AggregateRoot):
    title: str
