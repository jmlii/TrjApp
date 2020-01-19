from application import app, db
from flask import render_template, request
from application.kayttajat.models import Kayttaja

# Käyttäjien listaaminen
@app.route("/kayttajat", methods=["GET"])
def kayttajat_index():
    return render_template("kayttajat/list.html", kayttajat = Kayttaja.query.all())

# Uuden käyttäjän luominen
@app.route("/kayttajat/new")
def kayttajat_form():
    return render_template("/kayttajat/new.html")

# Luodun käyttäjän tiedot tietokantaan ja sivulle lisäämisen jälkeen
@app.route("/kayttajat/created", methods=["POST"])
def kayttajat_create():
    k = Kayttaja(request.form.get("etunimi"), 
    request.form.get("sukunimi"),
    request.form.get("kayttooikeustaso"), aktiivinen=True)
    
    db.session().add(k)
    db.session().commit()

    return "Tietokantaan lisätty: " + k.etunimi + " " + k.sukunimi + ", käyttöoikeustaso " + k.kayttooikeustaso + ", id " + str(k.id)

# Käyttäjän päättäminen
@app.route("/kayttajat/end<kayttaja_id>/", methods=["POST"])
def kayttajat_set_end(kayttaja_id): 
    k = Kayttaja.query.get(kayttaja_id)
    k.aktiivinen = False
    k.loppupvm = db.func.current_timestamp()
    db.session().commit()
    
    return "Käyttäjä päätetty järjestelmästä: id " + str(k.id) +", " + k.etunimi + " " + k.sukunimi