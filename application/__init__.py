# Tuodaan käyttöön Flask 
from flask import Flask
app = Flask(__name__)

# Tuodaan käyttöön SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Osoitetaan sovellus käyttämään Herokussa ollessa Herokun tietokantaa
import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
# Muulloin käytetään SQLite-tietokantaa nimeltä trj.db. 
# Tiedosto sijaitsee samassa kansiossa tämän sovelluksen tiedostojen kanssa.
else: 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trj.db"
    # Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Luetaan tiedostot models ja views sovelluksen eri kansioista
from application.wgroups import models
from application.wgroups import views

from application.auth import models
from application.auth import views

from application.roles import models
from application.roles import views

from application.rolerequests import models
from application.rolerequests import views

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


Luodaan tarvittavat tietokantataulut vain kerran
try:
    db.create_all()
except:
    pass
