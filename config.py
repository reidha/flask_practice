import argparse
import connexion
import os
import pathlib
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


CONFIGURATIONS: dict[str, str] = {
    'default': 'default.cfg',
    'prod': 'prod.cfg'
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="Configuration")
    parser.add_argument('-e', '--environment', default='default',
                        help="Environment (default / prod)")
    return parser.parse_args()


args = parse_args()

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app: Flask = connex_app.app  # type: ignore
app.config.from_pyfile(os.path.join(app.instance_path, CONFIGURATIONS[args.environment]))

db = SQLAlchemy(app)
ma = Marshmallow(app)
