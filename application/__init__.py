# Tuodaan käyttöön Flask 
from flask import Flask
app = Flask(__name__)

# Tuodaan käyttöön SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Käytetään SQLite-tietokantaa nimeltä kayttajat.db. 
# Tiedosto sijaitsee samassa kansiossa tämän sovelluksen tiedostojen kanssa.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kayttajat.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Luetaan kansiosta application/kayttajat tiedoston models sisältö
from application.kayttajat import models
from application.kayttajat import views

# Luodaan tarvittavat tietokantataulut
db.create_all()
