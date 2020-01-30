# Tuodaan käyttöön Flask 
from flask import Flask
app = Flask(__name__)

# Tuodaan käyttöön SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Käytetään SQLite-tietokantaa nimeltä trj.db. 
# Tiedosto sijaitsee samassa kansiossa tämän sovelluksen tiedostojen kanssa.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trj.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Luetaan kansiosta application/wgroups tiedoston models sisältö
from application.wgroups import models
from application.wgroups import views

# Luetaan kansiosta application/auth tiedoston models sisältö
from application.auth import models
from application.auth import views

# Kirjautuminen
from application.auth.models import User 
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan tarvittavat tietokantataulut
db.create_all()
