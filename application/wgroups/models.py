from application import db
from application.models import Base 
from sqlalchemy.sql import text

class Wgroup(Base):   
    name = db.Column(db.String(36), nullable=False)
    authoriser = db.Column(db.String(36), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    date_ended = db.Column(db.DateTime)

    rolerequests = db.relationship("Rolerequest", backref='wgroup', lazy=True)

    users = db.relationship("Membership", backref="wgroup")

    def __init__(self, name): 
        self.name = name

    @staticmethod
    def count_rolerequests_per_wgroup(approved, rejected, executed):
        stmt = text("SELECT Wgroup.name, COUNT(Wgroup.id) FROM Wgroup"
        " JOIN Rolerequest on Wgroup.id = Rolerequest.wgroup_id"
        " WHERE Rolerequest.approved = :approved AND Rolerequest.rejected = :rejected AND Rolerequest.executed = :executed"
        " GROUP BY Wgroup.name"
        " ORDER BY Wgroup.name").params(approved=approved, rejected=rejected, executed=executed)
        res  = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "number":row[1]})
        return response

    @staticmethod
    def list_members(wgroup_id):
        stmt = text("SELECT Account.last_name, Account.first_name, Account.username, Role.name"
        " FROM Account"
        " JOIN UserWgroupRole ON Account.id = UserWgroupRole.account_id"
        " JOIN Role ON UserWgroupRole.role_id = Role.id"
        " JOIN Wgroup on UserWgroupRole.wgroup_id = Wgroup.id"
        " WHERE Wgroup.id = :wgroup_id AND UserWgroupRole.date_ended IS NULL"
        " ORDER BY Account.last_name, Account.first_name").params(wgroup_id=wgroup_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"last_name":row[0], "first_name":row[1], "username":row[2], "role":row[3]})
        return response
