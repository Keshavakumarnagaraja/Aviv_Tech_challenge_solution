import pytest

from listingapi.domain import entities, use_cases
from tests import factories


class TestRetrieveListings:
    @pytest.fixture
    def listing_entity(self) -> entities.ListingEntity:
        listing_entity = (
            factories.entities.Listing()
            .with_name("Mikhail Schmiedt")
            .with_description("description")
            .with_building_type("APARTMENT")
            .with_rooms_count(6)
            .with_bedrooms_count(2)
            .with_surface_area_m2(167)
            .with_postal_address(
                factories.entities.PostalAddress()
                .with_street_address("Johan-Ernst-Ring 7")
                .with_postal_code("21810")
                .with_city("Berchtesgaden")
                .with_country("DE")
                .build()
            )
            .with_price(720000)
            .with_contact_phone_number("")
            .build()
        )

        return listing_entity

    
    def test_retrieve_listings(
        self,
        persist_listing_use_case: use_cases.PersistListing,
        retrieve_listing_use_case: use_cases.RetrieveListings,
        listing_entity: entities.ListingEntity,
    ) -> None:
        
        persist_listing_use_case.perform(listing_entity)
        retrieved_listing_dict_list = retrieve_listing_use_case.perform()
        
        retrieved_listing_dict = retrieved_listing_dict_list[0]
        assert retrieved_listing_dict["id"] == 1
        assert retrieved_listing_dict["name"] == "Mikhail Schmiedt"
        assert retrieved_listing_dict["postal_address"] == {
            "street_address": "Johan-Ernst-Ring 7",
            "postal_code": "21810",
            "city": "Berchtesgaden",
            "country": "DE",
        }
        assert retrieved_listing_dict["description"] == "description"
        assert retrieved_listing_dict["building_type"] == "APARTMENT"
        assert retrieved_listing_dict["latest_price_eur"] == 720000.0
        assert retrieved_listing_dict["surface_area_m2"] == 167
        assert retrieved_listing_dict["rooms_count"] == 6
        assert retrieved_listing_dict["bedrooms_count"] == 2
        assert retrieved_listing_dict["contact_phone_number"] == ""


