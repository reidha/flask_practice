import pathlib
import pytest
from app import create_app, db


@pytest.fixture(scope='module')
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f"sqlite:///{pathlib.Path(__file__).parent.resolve() / 'test.db'}"
    })

    with app.app_context():
        db.drop_all()
        db.create_all()

    yield app

    # db.drop_all()  # If you want to keep the test.db, comment out this line.


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()


@pytest.fixture(scope='module')
def runner(app):
    return app.test_cli_runner()
