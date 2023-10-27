from faker import Faker

from listingapi.domain import entities
from tests import factories


class ListingPriceLog:
    def __init__(self, locale: str = "fr-FR"):
        fake = Faker(locale)
        self.id = fake.random_int(100, 800)
        self.listing_id = fake.random_int(1, 10)
        self.date = fake.date_time_this_decade()
        self.price = float(fake.random_int(100_000, 2_000_000, 5000))

    def with_listing_id(self, id: int) -> "ListingPriceLog":
        self.listing_id = id
        return self

    def with_price(self, price: float) -> "ListingPriceLog":
        self.price = price
        return self

    def build(self) -> entities.ListingPriceLogEntity:
        return entities.ListingPriceLogEntity(
            id=self.id,
            listing_id=self.listing_id,
            date=self.date,
            price=self.price,
        )
