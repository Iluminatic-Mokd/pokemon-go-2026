from pokemon import create_app
from pokemon.extensions import db

app = create_app()

with app.app_context():
    db.create_all()
