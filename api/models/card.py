from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String

from api.models.base import BaseModel
from api.models.enums import CardType


class CardModel(BaseModel):

    __tablename__ = "cards"

    name = Column(String(128), nullable=False)
    type = Column(Enum(CardType), nullable=False)
    attack_strength = Column(Integer, nullable=False)
    defense_strength = Column(Integer, nullable=False)
    description = Column(String(256), nullable=False)
    image_filename = Column(String(128), nullable=False)