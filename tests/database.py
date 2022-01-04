from fastapi import testclient
from fastapi.testclient import TestClient
from sqlalchemy.sql.ddl import DDLBase
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db
from app.database import Base
import pytest


SQLALCHEMY_DATABASE_URL = f"{settings.database_prefix}://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_Test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def session():
    # delete the tables that were created previously
    Base.metadata.drop_all(bind=engine)

    # create the tables in the database
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    # override the get_db function
    app.dependency_overrides[get_db] = override_get_db
    
    # let the test continue
    yield TestClient(app)
