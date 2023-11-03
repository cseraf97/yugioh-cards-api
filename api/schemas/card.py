from marshmallow import (
    Schema,
    fields,
    pre_dump,
    pre_load,
    post_dump
)

from marshmallow_enum import EnumField

from api.models.enums import (
    CardType
)


class CardGetOneResponseSchema(Schema):
    """Schema to get one card response."""
    id = fields.Str()
    name = fields.Str()
    type = fields.Str()
    description = fields.Str()
    attack_strength = fields.Integer()
    defense_strength = fields.Integer()
    image_filename = fields.Str()

    @pre_dump
    def type_format(self, data, **args):
        data.type = CardType(data.type).name
        if data.type != CardType.MONSTER.name:
            del data.attack_strength
            del data.defense_strength
        return data

    @post_dump
    def strength_format(self, data, **args):
        if CardType[data['type']].name != CardType.MONSTER.name:
            data.pop('attack_strength')
            data.pop('defense_strength')
        return data

class CardGetAllResponseSchema(Schema):
    """Schema to get all cards response."""

    cards = fields.Nested(CardGetOneResponseSchema, many=True)


class CardGetAllRequestSchema(Schema):
    """Schema to get all cards request."""

    name = fields.Str()
    type = fields.Str()
    attack_strength = fields.Integer()
    defense_strength = fields.Integer()
    description = fields.Str()
    image_filename = fields.Str()


class CardCreateRequestSchema(Schema):
    """Schema to create card request."""

    id = fields.Str()
    name = fields.Str(required=True)
    type = EnumField(CardType, load_by=EnumField.NAME, required=True)
    description = fields.Str()
    attack_strength = fields.Integer()
    defense_strength = fields.Integer()
    image_filename = fields.Str(required=True)

    @pre_load
    def type_format(self, data, **args):
        data['type'] = data['type'].upper()
        return data
    
"""
    name = fields.Str(required=True)
    hp = fields.Integer(required=True)
    first_edition = fields.Boolean(required=True)
    expansion = EnumField(
        CardExpansion, load_by=EnumField.VALUE, required=True)
    type = EnumField(CardType, load_by=EnumField.VALUE, required=True)
    rarity = EnumField(CardRarity, load_by=EnumField.VALUE, required=True)
    price = fields.Integer(required=True)
    image_filename = fields.Str(required=True)

    @post_load
    def validate_hp(self, data, **args):
        hp = data.get('hp')
        if hp and hp % 10 != 0:
            raise ValueError("HP must be a multiple of 10")
        return data
    """


class CardUpdateRequestSchema(Schema):
    """Schema to update card request."""

    name = fields.Str()
    type = EnumField(CardType, load_by=EnumField.NAME)
    attack_strength = fields.Integer()
    defense_strength = fields.Integer()
    description = fields.Str()
    image_filename = fields.Str()
    
    @pre_load
    def type_format(self, data, **args):
        data['type'] = data['type'].upper()
        return data