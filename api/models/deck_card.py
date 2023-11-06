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

class DeckCardModel(BaseModel):

    __tablename__ = "decks_cards"

    deck_id: Mapped[int] = mapped_column(ForeignKey("decks.id"), primary_key=True)
    card_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), primary_key=True)
    card: Mapped["CardModel"] = relationship(back_populates="decks")
    deck: Mapped["DeckModel"] = relationship(back_populates="cards")