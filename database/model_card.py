from .base import Base
from .model_task import ModelTask
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import backref, relationship


class ModelCard(Base):
    """Модель карточки"""

    __tablename__ = 'cards'

    id = Column('id', Integer, primary_key=True, doc="Id для карточки")
    card_name = Column('card_name', String, doc="Название карточки")
    created = Column('created', DateTime, default=func.now(), doc="Запись даты создания карточки")

    # taskList = relationship(ModelTask, backref=backref('tasks', uselist=True, cascade='delete-orphan,all'))
    taskList = relationship(ModelTask, cascade="all,delete-orphan", backref="card")
