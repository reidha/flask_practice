from app.api.people import read_all, create


def test_create(app):
    with app.app_context():
        result, _ = create({'fname': 'Taro', 'lname': 'Yamada'})
    assert result['lname'] == 'Yamada'  # type: ignore


def test_read_all(app):
    with app.app_context():
        result = read_all()
    assert len(result) == 1
