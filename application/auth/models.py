from application import db
from application.models import Base 
from application.permissions.models import Permission
from sqlalchemy.sql import text

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

    @staticmethod
    def list_memberships(user_id):
        stmt = text("SELECT Wgroup.name, Role.name, Wgroup.date_created"
        " FROM Wgroup"
        " JOIN UserWgroupRole ON Wgroup.id = UserWgroupRole.wgroup_id"
        " JOIN Role ON UserWgroupRole.role_id = Role.id"
        " JOIN Account on UserWgroupRole.account_id = Account.id"
        " WHERE Account.id = :user_id AND UserWgroupRole.date_ended IS NULL"
        " ORDER BY Wgroup.name").params(user_id=user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"wgroup":row[0], "role":row[1], "date_created":row[2]})
        return response
    