import pytest
from sqlalchemy.exc import (
    IntegrityError,
    InvalidRequestError,
    CompileError
)

from api.exceptions import NotFoundError
from api.services.card import CardService
from api.utils.testing import DBTest


class TestCardService(DBTest):
    def setUp(self):
        self.card_payload = {
            "name": "Dark Magician",
            "type": "SPELL",
            "description": "Dark Magicians is one of Yugi's signature monsters, knwn for its powerful spellcasting abilities and iconic design.",
            "image_filename": "dark_magician.jpg"
        }

    def test_create_card_success(self):
        card = CardService.create(self.card_payload)
        assert card

    def test_create_card_error_missing_fields(self):
        with pytest.raises(IntegrityError):
            CardService.create({"type": "SPELL"})

    def test_update_card_success(self):
        card = CardService.create(self.card_payload)
        new_name = "new_name"
        card = CardService.update(card.id, {"name": new_name})
        assert card.name == new_name

    def test_update_card_error_unkown_value(self):
        card = CardService.create(self.card_payload)
        with pytest.raises(CompileError):
            CardService.update(card.id, {"foo": "foo"})

    def test_get_one_card_success(self):
        card = CardService.create(self.card_payload)
        card = CardService.get_one(card.id)
        assert card.id

    def test_get_one_card_error_not_found(self):
        random_uuid = "93fb3b57-1895-4f7b-ab8a-6853de44f606"
        with pytest.raises(NotFoundError):
            CardService.get_one(random_uuid)

    def test_get_many_cards_success(self):
        payload_one = self.card_payload.copy()
        CardService.create(payload_one)

        response = CardService.get_many({})
        assert len(response['cards']) == 1

    def test_get_many_cards_error_not_found(self):
        filters = {"type": "SPELL"}
        response = CardService.get_many(filters)
        assert len(response['cards']) == 0

    def test_delete_card_success(self):
        card = CardService.create(self.card_payload)
        CardService.delete(card.id)
        with pytest.raises(NotFoundError):
            CardService.get_one(card.id)

    def test_delete_card_error_not_found(self):
        random_uuid = "93fb3b57-1895-4f7b-ab8a-6853de44f606"
        with pytest.raises(NotFoundError):
            CardService.delete(random_uuid)