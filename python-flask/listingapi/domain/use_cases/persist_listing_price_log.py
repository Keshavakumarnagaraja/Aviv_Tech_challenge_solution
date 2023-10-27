from listingapi.domain import entities, ports


class PersistListingPriceLog:
    def __init__(self, listing_price_log_repository: ports.ListingPriceLogRepository):
        self.listing_price_log_repository = listing_price_log_repository

    def perform(self, listing_price_log: entities.ListingPriceLogEntity) -> dict:
        listing_dict = self.listing_price_log_repository.create(listing_price_log)
        return listing_dict
