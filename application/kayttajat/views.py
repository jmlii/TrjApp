from application import app, db
from flask import render_template, request
from application.kayttajat.models import Kayttaja

@app.route("/kayttajat", methods=["GET"])
def kayttajat_index():
    return render_template("kayttajat/list.html", kayttajat = Kayttaja.query.all())

@app.route("/kayttajat/new")
def kayttajat_form():
    return render_template("/kayttajat/new.html")

@app.route("/kayttajat/created", methods=["POST"])
def kayttajat_create():
    k = Kayttaja(request.form.get("etunimi"), 
    request.form.get("sukunimi"),
    request.form.get("kayttooikeustaso"))

    db.session().add(k)
    db.session().commit()

    return "Tietokantaan lisätty: " + k.etunimi + " " + k.sukunimi + ", käyttöoikeustaso " + k.kayttooikeustaso + ", id " + str(k.id)
