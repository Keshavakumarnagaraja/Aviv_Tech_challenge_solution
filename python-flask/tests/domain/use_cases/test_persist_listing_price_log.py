import pytest
from freezegun import freeze_time

from listingapi.domain import entities, use_cases
from tests import factories


class TestPersistListingPriceLog:
    @pytest.fixture
    def listing_price_log_entity(self) -> entities.ListingPriceLogEntity:
        listing_price_log_entity = (
            factories.entities.ListingPriceLog()
            .with_listing_id(10)
            .with_price(170000)
            .build()
        )

        return listing_price_log_entity

    def test_persist_listing_price_log(
        self,
        persist_listing_price_log_use_case: use_cases.PersistListingPriceLog,
        listing_price_log_entity: entities.ListingPriceLogEntity,
    ) -> None:
        persist_listing_price_log_dict = persist_listing_price_log_use_case.perform(
            listing_price_log_entity
        )
        print(persist_listing_price_log_dict)
        assert persist_listing_price_log_dict["price"] == 170000
