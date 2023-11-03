from flask import Flask

from api.config import Config
from api.utils.db import init_db



def create_app(config):
    """Initialize api db."""

    app = Flask(__name__)
    app.config.from_object(config)

    init_db(app)

    @app.route('/')
    def _():
        return "It works!"

    return app


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="0.0.0.0", debug=True)
