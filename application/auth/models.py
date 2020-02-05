from application import db
from application.models import Base 

class User(Base): #(db.Model):

    __tablename__ = "account"

    # id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(144), nullable=False)
    last_name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    account_active = db.Column(db.Boolean, nullable=False, default=True)
    # date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    # date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    #    onupdate=db.func.current_timestamp())
    date_inactivated = db.Column(db.DateTime)

    rolerequests = db.relationship("Rolerequest", backref='account', lazy=True)

    
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    def get_id(self):
        return self.id
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True

