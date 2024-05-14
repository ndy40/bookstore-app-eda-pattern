from datetime import datetime

from bookstore.core.domain.models import AggregateRoot


class CheckoutDetails:
    user_id: str
    checkout_date: datetime.date
    expected_return_date: datetime.date
    duration_in_days: int


class ReservationDetails:
    copies: int
    available: int
    last_checkout: list
    checkout_history: list[CheckoutDetails]


class Book(AggregateRoot):
    book_id: str
    title: str
    location: str
    classification: str
    available: bool
    description: str
    reservation: ReservationDetails
