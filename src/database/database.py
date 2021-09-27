from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..settings import settings

from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = settings.SQL_DB

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
