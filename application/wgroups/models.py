from application import db
from application.models import Base 

class Wgroup(Base):  #(db.Model):
    # id = db.Column(db.Integer, primary_key=True)   
    name = db.Column(db.String(36), nullable=False)
    authoriser = db.Column(db.String(36), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    # date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    # date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    # onupdate=db.func.current_timestamp())
    date_ended = db.Column(db.DateTime)

    rolerequests = db.relationship("Rolerequest", backref='wgroup', lazy=True)


    def __init__(self, name): #, authoriser):
        self.name = name
    #   self.authoriser = authoriser
