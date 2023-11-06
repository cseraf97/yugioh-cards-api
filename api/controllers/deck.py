from flask import request

from flask_restful import Resource

from api.schemas.deck import (
    DeckGetOneResponseSchema,
    DeckGetAllRequestSchema,
    DeckGetAllResponseSchema,
    DeckCreateRequestSchema,
    DeckCardUpdateRequestSchema,
    DeckUpdateRequestSchema
)
from api.services.deck import DeckService
from api.services.deck_card import DeckCardService
from api.services.card import CardService

class DeckCardController(Resource):
    """Exposes get and create REST methods."""

    def post(self):
        """Associate a card with a deck by card id and deck id."""

        payload = request.get_json()
        DeckCardUpdateRequestSchema().load(payload)
        CardService.get_one(card_id=payload["card_id"])
        DeckService.get_one(deck_id=payload["deck_id"])
        DeckCardService.associate(payload)
        return "The card has been associated", 200

    def delete(self):
        """Associate a card with a deck by card id and deck id."""

        payload = request.get_json()
        DeckCardUpdateRequestSchema().load(payload)
        CardService.get_one(card_id=payload["card_id"])
        DeckService.get_one(deck_id=payload["deck_id"])
        DeckCardService.disassociate(card_id=payload["card_id"], deck_id=payload["deck_id"])
        return "The card has been disassociated", 200

class SingleDeckController(Resource):
    """Exposes get and create REST methods."""

    def get(self):
        """Retrieve many decks by filters."""

        filters = request.args
        DeckGetAllRequestSchema().load(filters)
        decks = DeckService.get_many(filters)
        return DeckGetAllResponseSchema().dump(decks), 200

    def post(self):
        """Create a deck."""

        payload = request.get_json()
        DeckCreateRequestSchema().load(payload)
        deck = DeckService.create(payload)
        return DeckGetOneResponseSchema().dump(deck), 201


class SingleDeckIDController(Resource):
    """Exposes get, update and delete REST methods."""

    def get(self, deck_id):
        """Retrieve a deck by id."""

        deck = DeckService.get_one(deck_id)
        # deck = DeckCardService.get_cards_in_deck(deck_id)
        return DeckGetOneResponseSchema().dump(deck), 200

    def put(self, deck_id):
        """Update a deck by id."""

        payload = request.get_json()
        DeckUpdateRequestSchema().load(payload)
        deck = DeckService.update(deck_id, payload)
        return DeckGetOneResponseSchema().dump(deck), 200

    def delete(self, deck_id):
        """Delete a deck by id."""
        DeckCardService.delete_by_deck_id(deck_id=deck_id)
        DeckService.delete(deck_id)
        return None, 204