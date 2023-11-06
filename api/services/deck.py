from api.db import db
from api.models.deck import DeckModel
from api.models.deck_card import DeckCardModel
from api.exceptions import NotFoundError


class DeckService:
    """Manage deck model."""

    _model = DeckModel

    @classmethod
    def create(cls, deck_payload):
        """Creates deck."""

        model = cls._model(**deck_payload)
        db.session.add(model)
        db.session.commit()
        return model

    @classmethod
    def update(cls, deck_id, deck_payload):
        """Updates a deck."""
        db.session.query(cls._model).filter_by(id=deck_id).update(deck_payload)
        db.session.commit()
        deck = cls.get_one(deck_id)
        return deck

    @classmethod
    def get_one(cls, deck_id):
        """Retrieves a deck by filters."""

        deck = cls._model.query.get(deck_id)
        if not deck:
            raise NotFoundError(f"The deck {deck_id} was not found")
        return deck

    @classmethod
    def get_many(cls, filters):
        """Retrieves many decks by filters."""

        decks = cls._model.query.filter_by(**filters).all()
        return {"decks": decks}

    @classmethod
    def delete(cls, deck_id):
        """Deletes a deck."""

        deck = cls.get_one(deck_id)
        db.session.delete(deck)
        db.session.commit()
