from flask import render_template

from app import app
from models.person import Person


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)
