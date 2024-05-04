from bookstore.core.domain.models import AggregateRoot


class Book(AggregateRoot):
    title: str
