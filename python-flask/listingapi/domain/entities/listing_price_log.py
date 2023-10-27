from pydantic import BaseModel
from datetime import date


class ListingPriceLogEntity(BaseModel):
    id: int
    listing_id: int
    date: date
    price: float
