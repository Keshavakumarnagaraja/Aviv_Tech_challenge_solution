from listingapi.domain import ports


class RetrieveListingsPriceLogByListingId:
    def __init__(self, listing_price_log_repository: ports.ListingPriceLogRepository):
        self.listing_price_log_repository = listing_price_log_repository

    def perform(self, listing_id: int) -> list[dict]:
        listings = self.listing_price_log_repository.get_all_by_listing_id(listing_id)
        return listings
