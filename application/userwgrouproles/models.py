from application import db
from sqlalchemy.sql import text

class Membership(db.Model):
    __tablename__ = "userwgrouprole"

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False, primary_key=True)
    wgroup_id = db.Column(db.Integer, db.ForeignKey("wgroup.id"), nullable=False, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp(), primary_key=True)
    date_ended = db.Column(db.DateTime)

    user = db.relationship("User", backref="wgroups")


    def __init__(self, account_id, wgroup_id, role_id):
        self.account_id = account_id
        self.wgroup_id = wgroup_id
        self.role_id = role_id
  
    @staticmethod
    def list_memberships():
        stmt = text("SELECT Account.username, Wgroup.name, Role.name,"
        " UserWgroupRole.date_created, UserWgroupRole.date_ended," 
        " UserWgroupRole.account_id, UserWgroupRole.wgroup_id, UserWgroupRole.role_id "
        " FROM Wgroup"
        " JOIN UserWgroupRole ON Wgroup.id = UserWgroupRole.wgroup_id"
        " JOIN Role ON UserWgroupRole.role_id = Role.id"
        " JOIN Account on UserWgroupRole.account_id = Account.id"
        " ORDER BY UserWgroupRole.date_created DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"user":row[0], "wgroup":row[1], "role":row[2], 
                "date_created":row[3], "date_ended":row[4], "account_id":row[5],
                "wgroup_id":row[6], "role_id":row[7]})
        return response    
