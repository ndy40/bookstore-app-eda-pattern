# Book Creation

## Book Management Module (book_mgt):

Role: Responsible for adding books to the database.

### Event Details

**BookCreated**

*Actions Triggered*

1. Add book to catalogue.
2. Update Reservation records.

*Event Triggered*

1. BookAddedToCatalogue
2. BookAddedToReservation

---
**BookUpdated**

*Actions*

1. Update Book records in catalogue.
2. Update reservation records.

*Events*

1. CatalogueUpdated
2. ReservationUpdated

---
