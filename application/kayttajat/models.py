from application import db

class Kayttaja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    etunimi = db.Column(db.String(36), nullable=False)
    sukunimi = db.Column(db.String(36), nullable=False)
    kayttooikeustaso = db.Column(db.String(18), nullable=False)
    aktiivinen = db.Column(db.Boolean, nullable=False, default=True)
    luontipvm = db.Column(db.DateTime, default=db.func.current_timestamp())
    muokkauspvm = db.Column(db.DateTime, default=db.func.current_timestamp(), 
    onupdate=db.func.current_timestamp())
    loppupvm = db.Column(db.DateTime)

    def __init__(self, etunimi, sukunimi, kayttooikeustaso, aktiivinen):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.kayttooikeustaso = kayttooikeustaso
        self.aktiivinen = aktiivinen
