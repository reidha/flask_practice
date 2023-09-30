import connexion
import os
import pathlib
import prance
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from pathlib import Path
from typing import Any


BASE_DIR = pathlib.Path(__file__).parent.resolve()
db = SQLAlchemy()
ma = Marshmallow()


def get_bundled_specs(main_file: Path) -> dict[str, Any]:
    parser = prance.ResolvingParser(str(main_file.absolute()),
                                    lazy=True, backend='openapi-spec-validator')
    parser.parse()
    return parser.specification  # type: ignore


def create_app(config_class: str = ''):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')

    connex_app = connexion.App(__name__, specification_dir=BASE_DIR)
    app: Flask = connex_app.app  # type: ignore

    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object(f"configurations.{config_name}_config.{config_name.capitalize()}Config")

    db.init_app(app)
    ma.init_app(app)

    connex_app.add_api(get_bundled_specs(BASE_DIR / "openapi/main.yml"))
    return app
