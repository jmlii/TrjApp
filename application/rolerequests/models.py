from application import db
from application.models import Base

class Rolerequest(Base):
    request_type = db.Column(db.String(32), nullable=False)
    justification = db.Column(db.String(256))
    approved = db.Column(db.Boolean, default=False)
    date_approved = db.Column(db.DateTime, default=db.func.current_timestamp())
    rejected = db.Column(db.Boolean, default=False)
    date_rejected = db.Column(db.DateTime, default=db.func.current_timestamp())
    executed = db.Column(db.Boolean, default=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), 
        nullable=False)
    wgroup_id = db.Column(db.Integer, db.ForeignKey('wgroup.id'), 
        nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), 
        nullable=False)


    def __init__(self, request_type):
        self.request_type = request_type


  
        