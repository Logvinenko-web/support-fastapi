import uuid

from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from src.database.database import Base


def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = 'users'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    path = Column(String, nullable=False)

    documentation = relationship("Documentations")


class Documentations(Base):
    __tablename__ = 'documentations'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    description = Column(String, nullable=False)

    category_id = Column(String, ForeignKey('categories.id'))

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    title =Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
