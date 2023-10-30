import connexion
import os
import pathlib
import prance
from flask.app import Flask
from logging.config import dictConfig
from pathlib import Path
from typing import Any

from app.models import db, ma


BASE_DIR = pathlib.Path(__file__).parent.resolve()
LOG_DIR = os.path.join(BASE_DIR, '..', 'logs')


def get_bundled_specs(main_file: Path) -> dict[str, Any]:
    parser = prance.ResolvingParser(str(main_file.absolute()),
                                    lazy=True, backend='openapi-spec-validator')
    parser.parse()
    return parser.specification  # type: ignore


def get_logging_config(config_name: str) -> dict[str, Any]:
    return {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            }
        },
        'handlers': {
            'file': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOG_DIR, 'flask.log'),
                'formatter': 'default',
                'when': 'D',
                'backupCount': 0,
                'utc': True,
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG' if config_name == 'default' else 'INFO',
                'handlers': ['file', 'console']
            }
        },
    }


def create_app(test_config: dict = {}):
    connex_app = connexion.App(__name__, specification_dir=BASE_DIR)
    app: Flask = connex_app.app  # type: ignore

    app.config.from_prefixed_env()
    config_name = app.config.get("CONFIG", 'default')

    os.makedirs(LOG_DIR, exist_ok=True)
    dictConfig(get_logging_config(config_name))

    app.config.from_object(f"app.configurations.{config_name}_config.{config_name.capitalize()}Config")
    app.config.from_pyfile(os.path.join(app.instance_path, f"{config_name}.cfg"), silent=True)
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    ma.init_app(app)

    connex_app.add_api(get_bundled_specs(BASE_DIR / "openapi/main.yml"))
    return app
