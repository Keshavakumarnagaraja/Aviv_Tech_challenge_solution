from listingapi.adapters.sql_alchemy_listing_price_log_repository.models import ListingPriceLogModel
from listingapi.domain import entities


class ListingPriceLogMapper:
    @staticmethod
    def from_entity_to_model(listing_price_log: entities.ListingPriceLogEntity) -> ListingPriceLogModel:
        listing_price_log_model = ListingPriceLogModel(
            id=listing_price_log.id,  
            listing_id=listing_price_log.listing_id,  
            updated_time=listing_price_log.date,   
            price=listing_price_log.price,
        )
        return listing_price_log_model

    @staticmethod
    def from_model_to_dict(listing_price_log_model: ListingPriceLogModel) -> dict:
        listing_dict = {
            "date": listing_price_log_model.updated_time.strftime("%Y/%m/%d, %H:%M:%S"),
            "price": listing_price_log_model.price,
        }
        return listing_dict
