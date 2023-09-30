import prance
from flask import render_template
from pathlib import Path
from typing import Any

import config
from models.person import Person


def get_bundled_specs(main_file: Path) -> dict[str, Any]:
    parser = prance.ResolvingParser(str(main_file.absolute()),
                                    lazy=True, backend='openapi-spec-validator')
    parser.parse()
    return parser.specification  # type: ignore


app = config.connex_app
app.add_api(get_bundled_specs(config.basedir / "openapi/main.yml"))


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
