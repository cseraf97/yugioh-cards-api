from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from api.models.base import BaseModel

from typing import List

class DeckModel(BaseModel):

    __tablename__ = "decks"

    name = Column(String(128), unique=True, nullable=False)
    cards: Mapped[List["DeckCardModel"]] = relationship(back_populates="deck")