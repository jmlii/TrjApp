from application import db
from application.models import Base 
from application.permissions.models import Permission

class User(Base): 

    __tablename__ = "account"

    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    account_active = db.Column(db.Boolean, nullable=False, default=True)
    date_inactivated = db.Column(db.DateTime)

    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'), 
        nullable=False)

    rolerequests = db.relationship("Rolerequest", backref='account', lazy=True)
    
    def __init__(self, username):
        self.username = username
    
    def get_id(self):
        return self.id
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True

    def permission_name(self):
        permission = Permission.query.filter_by(id=self.permission_id).first()
        return permission.name

    def permissions(self):
        permission = Permission.query.filter_by(id=self.permission_id).first()
        return [permission.name]