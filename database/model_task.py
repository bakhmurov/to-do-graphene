from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class ModelTask(Base):
    """Модель задачи"""

    __tablename__ = 'tasks'

    id = Column('id', Integer, primary_key=True, doc="Id задачи")
    task_name = Column('task_name', String, doc="Название задачи")
    card_id = Column('card_id', Integer, ForeignKey('cards.id'), doc="Id карточки")


