from flask import Flask

from api.config import Config
from api.controllers.card import (
    SingleCardController,
    SingleCardIDController
)
from api.controllers.deck import (
    SingleDeckController,
    SingleDeckIDController,
    DeckCardController
)
from api.utils.api import BaseAPI
from api.utils.db import init_db



def create_app(config):
    """Initialize api db."""

    app = Flask(__name__)
    app.config.from_object(config)

    init_db(app)

    @app.route('/')
    def index():
        return "It works!"

    api = BaseAPI(app)
    api.add_resource(SingleCardController, '/cards')
    api.add_resource(SingleCardIDController, '/cards/<card_id>')
    api.add_resource(SingleDeckController, '/decks')
    api.add_resource(SingleDeckIDController, '/decks/<deck_id>')
    api.add_resource(DeckCardController, '/decks/cards')

    return app


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="0.0.0.0", debug=True)
