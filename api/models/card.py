from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from api.models.base import BaseModel
from api.models.enums import CardType


class CardModel(BaseModel):

    __tablename__ = "cards"

    name = Column(String(128), unique=True, nullable=False)
    type = Column(Integer, nullable=False)
    attack_strength = Column(Integer, nullable=True)
    defense_strength = Column(Integer, nullable=True)
    description = Column(String(256), nullable=False)
    image_filename = Column(String(128), nullable=False)
    decks: Mapped["DeckCardModel"] = relationship(back_populates="card")