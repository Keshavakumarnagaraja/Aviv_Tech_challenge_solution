import pytest

from listingapi.domain import entities, use_cases
from tests import factories


class TestRetrieveListingPriceLogByListingId:
    @pytest.fixture
    def listing_price_log_entities(self) -> entities.ListingPriceLogEntity:
        listing_price_log_entities = []
        listing_price_log_entity1 = (
            factories.entities.ListingPriceLog()
            .with_listing_id(3)
            .with_price(170000)
            .build()
        )
        listing_price_log_entity2 = (
            factories.entities.ListingPriceLog()
            .with_listing_id(3)
            .with_price(180000)
            .build()
        )
        listing_price_log_entity3 = (
            factories.entities.ListingPriceLog()
            .with_listing_id(3)
            .with_price(190000)
            .build()
        )
        listing_price_log_entities.append(listing_price_log_entity1)
        listing_price_log_entities.append(listing_price_log_entity2)
        listing_price_log_entities.append(listing_price_log_entity3)

        return listing_price_log_entities

    
    def test_retrieve_listing_price_log_by_listing_id(
        self,
        persist_listing_price_log_use_case: use_cases.PersistListingPriceLog,
        retrieve_listing_price_log_by_listing_id_use_case: use_cases.RetrieveListingsPriceLogByListingId,
        listing_price_log_entities: entities.ListingPriceLogEntity,
    ) -> None:
        for listing_price_log_entity in listing_price_log_entities:
            persist_listing_price_log_use_case.listing_price_log_repository.create(
                listing_price_log_entity
            )
        retrieve_listing_price_log_dict_list = retrieve_listing_price_log_by_listing_id_use_case.listing_price_log_repository.get_all_by_listing_id(3)

        prices = [item['price'] for item in retrieve_listing_price_log_dict_list]
        
        assert len(retrieve_listing_price_log_dict_list) == 3
        assert sorted(prices) == [170000.0, 180000.0, 190000.0]
        
    
    def test_retrieve_listing_price_log_by_listing_id_with_non_existing_listing_id(
        self,
        retrieve_listing_price_log_by_listing_id_use_case: use_cases.RetrieveListingsPriceLogByListingId,
    ) -> None:
        retrieve_listing_price_log_dict_list = retrieve_listing_price_log_by_listing_id_use_case.perform(100)

        assert len(retrieve_listing_price_log_dict_list) == 0



