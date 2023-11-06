from api.db import db
from api.models.deck_card import DeckCardModel
from api.exceptions import NotFoundError

class DeckCardService:
    """Manage deck model."""

    _model = DeckCardModel

    @classmethod
    def associate(cls, deck_payload):
        """Associate a card with a deck."""

        existing_association = db.session.query(cls._model).filter_by(deck_id=deck_payload["deck_id"], card_id=deck_payload["card_id"]).first()

        if existing_association:
            raise NotFoundError(f"The association with deck {deck_payload['deck_id']} and card {deck_payload['card_id']} already exists")
        else:
            new_association = cls._model(deck_id=deck_payload["deck_id"], card_id=deck_payload["card_id"])
            db.session.add(new_association)
            db.session.commit()

    @classmethod
    def get_one(cls, deck_id):
        """Retrieves a card by filters."""

        deck = cls._model.query.get(deck_id)
        if not card:
            raise NotFoundError(f"The deck {deck_id} was not found")
        return card

    @classmethod
    def disassociate(cls, card_id, deck_id):
        """Disassociate a card from its deck."""

        # Find the association to be removed
        association_to_remove = db.session.query(cls._model).filter_by(card_id=card_id, deck_id=deck_id).first()

        if association_to_remove:
            # If the association exists, delete it and commit the changes
            db.session.delete(association_to_remove)
            db.session.commit()
        else:
            raise NotFoundError(f"There is no association between card {card_id} and deck {deck_id}")

    @classmethod
    def get_cards_in_deck(cls, deck_id):
        """Retrieve the cards in a specific deck."""
        cards_in_deck = db.session.query(cls._model.card_id).filter_by(deck_id=deck_id).all()

        # Extract the card IDs from the query result and return them as a list.
        card_ids = [card[0] for card in cards_in_deck]

        return card_ids

    
    @classmethod
    def delete_by_deck_id(cls, deck_id):
        """."""
        db.session.query(cls._model).filter_by(deck_id=deck_id).delete(synchronize_session=False)

