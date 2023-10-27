from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.exc import NoResultFound
from listingapi.adapters.sql_alchemy_listing_price_log_repository import mappers, models
from listingapi.domain import entities, ports



class SqlAlchemyListingPriceLogRepository(ports.ListingPriceLogRepository):
    def __init__(self, db_session: scoped_session):
        self.db_session = db_session

    def init(self) -> None:
        models.Base.metadata.create_all(self.db_session.get_bind())

    def create(self, listing_price_log: entities.ListingPriceLogEntity) -> dict:
        listing_price_log_model = mappers.ListingPriceLogMapper.from_entity_to_model(listing_price_log)
        self.db_session.add(listing_price_log_model)
        self.db_session.commit()
        data = mappers.ListingPriceLogMapper.from_model_to_dict(listing_price_log_model)
        return data

    def get_all(self) -> list[dict]:
        #Not Required
        return

    def update(self, listing_id: int, listing: entities.ListingEntity) -> dict:
        #Not Required
        return 
    
    def get_all_by_listing_id(self, listing_id: int) -> list[dict]:
        try:
            listing_price_log_models = (
                self.db_session.query(models.ListingPriceLogModel)
                .filter(models.ListingPriceLogModel.listing_id == listing_id)
                .all()
            )
            listing_price_logs = [
                mappers.ListingPriceLogMapper.from_model_to_dict(listing_price_log)
                for listing_price_log in listing_price_log_models
            ]
            return listing_price_logs
        except NoResultFound:
            # Handle the case where no records are found for the given listing_id
            return []