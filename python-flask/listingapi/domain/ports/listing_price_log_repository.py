import abc

from listingapi.domain import entities


class ListingPriceLogRepository(abc.ABC):
    @abc.abstractmethod
    def init(self) -> None:
        pass

    @abc.abstractmethod
    def create(self, price_log: entities.ListingPriceLogEntity) -> dict:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[dict]:
        pass

    @abc.abstractmethod
    def update(self, id_: int, price_log: entities.ListingPriceLogEntity) -> dict:
        pass
    
    @abc.abstractmethod
    def get_all_by_listing_id(self, listing_id: int) -> list[dict]:
        pass