import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from listingapi import adapters
from listingapi.domain import ports, use_cases


@pytest.fixture
def db_session() -> scoped_session:
    in_memory_engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    _session_factory = sessionmaker(
        autocommit=False, autoflush=True, bind=in_memory_engine
    )
    db_session: scoped_session = scoped_session(_session_factory)
    return db_session


@pytest.fixture
def listing_repository(db_session: scoped_session) -> ports.ListingRepository:
    listing_repository = adapters.SqlAlchemyListingRepository(db_session)
    listing_repository.init()
    return listing_repository

@pytest.fixture
def listing_price_log_repository(db_session: scoped_session) -> ports.ListingPriceLogRepository:
    listing_price_log_repository = adapters.SqlAlchemyListingPriceLogRepository(db_session)
    listing_price_log_repository.init()
    return listing_price_log_repository


@pytest.fixture
def persist_listing_use_case(
    listing_repository: ports.ListingRepository,
) -> use_cases.PersistListing:
    return use_cases.PersistListing(listing_repository)

@pytest.fixture
def retrieve_listing_use_case(
    listing_repository: ports.ListingRepository,
) -> use_cases.RetrieveListings:
    return use_cases.RetrieveListings(listing_repository)


@pytest.fixture
def update_listing_use_case(
    listing_repository: ports.ListingRepository,
) -> use_cases.UpdateListing:
    return use_cases.UpdateListing(listing_repository)


@pytest.fixture
def retrieve_listing_price_log_by_listing_id_use_case(
    listing_price_log_repository: ports.ListingPriceLogRepository,
) -> use_cases.RetrieveListingsPriceLogByListingId:
    return use_cases.RetrieveListingsPriceLogByListingId(listing_price_log_repository)


@pytest.fixture
def persist_listing_price_log_use_case(
     listing_price_log_repository: ports.ListingPriceLogRepository,
) -> use_cases.PersistListingPriceLog:
    return use_cases.PersistListingPriceLog(listing_price_log_repository)


