from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class ListingPriceLogModel(Base):
    __tablename__ = "listing_price_log"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    listing_id: int = Column(Integer, nullable=False)
    updated_time: datetime = Column(
        DateTime, default=lambda: datetime.utcnow(), nullable=False
    )
    # price
    price: float = Column(Float, nullable=False)