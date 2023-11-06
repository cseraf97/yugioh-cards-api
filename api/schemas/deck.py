from marshmallow import (
    Schema,
    fields,
    pre_dump,
    pre_load,
    post_dump
)


class DeckCardNestedResponseSchema(Schema):
    """Schema to get one deck response."""
    card_id = fields.Str(data_key="id")

class DeckGetOneResponseSchema(Schema):
    """Schema to get one deck response."""
    id = fields.Str()
    name = fields.Str()
    cards = fields.Nested(DeckCardNestedResponseSchema, many=True)

class DeckGetAllResponseSchema(Schema):
    """Schema to get all decks response."""

    decks = fields.Nested(DeckGetOneResponseSchema, many=True)

class DeckGetAllRequestSchema(Schema):
    """Schema to get all decks request."""

    name = fields.Str()


class DeckUpdateRequestSchema(Schema):
    """Schema to update deck request."""

    name = fields.Str()

class DeckCardUpdateRequestSchema(Schema):
    id = fields.Str()
    card_id = fields.Str()
    deck_id = fields.Str()


class DeckCreateRequestSchema(Schema):
    """Schema to create deck request."""

    name = fields.Str(required=True)