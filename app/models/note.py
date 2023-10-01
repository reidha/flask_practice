from datetime import datetime

from app import db, ma


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, content, timestamp=None) -> None:
        self.content = content
        if timestamp is not None:
            self.timestamp = timestamp


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True


note_schema = NoteSchema()
