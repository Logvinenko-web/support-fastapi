import uuid

from sqlalchemy import String, Integer, Text
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
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)



class Education_Days(Base):
    __tablename__ = 'education_days'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    day = Column(String, nullable=False)
    education_task = relationship("Education_Tasks")


class Education_Tasks(Base):
    __tablename__ = 'education_tasks'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
    description = Column(String, nullable=False)
    education_day_id = Column(String, ForeignKey('education_days.id'))


class Tabs(Base):
    __tablename__ = 'tabs'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    category_id = Column(String, ForeignKey('categories.id'))


class Explanation(Base):
    __tablename__ = 'explanation'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    description = Column(Text, nullable=False)
    category_id = Column(String, ForeignKey('categories.id'))
    tab_id = Column(String, ForeignKey('tabs.id'))


class Instructions(Base):
    __tablename__ = 'instructions'

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
    category_id = Column(String, ForeignKey('categories.id'))
    tab_id = Column(String, ForeignKey('tabs.id'))