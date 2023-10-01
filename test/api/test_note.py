from app.api.people import create as people_create
from app.api.notes import read_one, create


def test_create(app):
    with app.app_context():
        people_create({'fname': 'Hanako', 'lname': 'Kato'})
        result, _ = create({'person_id': 1, 'content': 'test'})
    assert result['content'] == 'test'  # type: ignore


def test_read_one_001(app):
    with app.app_context():
        result = read_one(1)
    assert result['content'] == 'test'  # type: ignore
