from application import db
from application.models import Base
from sqlalchemy.sql import text

class Rolerequest(Base):
    request_type = db.Column(db.String(32), nullable=False)
    justification = db.Column(db.String(256))
    approved = db.Column(db.Boolean, default=False)
    date_approved = db.Column(db.DateTime)
    rejected = db.Column(db.Boolean, default=False)
    date_rejected = db.Column(db.DateTime)
    executed = db.Column(db.Boolean, default=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), 
        nullable=False)
    wgroup_id = db.Column(db.Integer, db.ForeignKey('wgroup.id'), 
        nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), 
        nullable=False)


    def __init__(self, request_type):
        self.request_type = request_type

    @staticmethod
    def list_rolerequests():
        stmt = text("SELECT Rolerequest.id, Rolerequest.request_type,"
        " Account.username, Wgroup.name, Role.name, Rolerequest.justification,"
        " Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved,"
        " Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed," 
        " Rolerequest.date_created, Rolerequest.date_modified"
        " FROM Rolerequest"
        " JOIN Account ON Rolerequest.account_id = Account.id "
        " JOIN Role ON Rolerequest.role_id = Role.id"
        " JOIN Wgroup ON Rolerequest.wgroup_id = Wgroup.id"
        " ORDER BY Rolerequest.date_created")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "request_type":row[1], "user":row[2], 
                "wgroup":row[3], "role":row[4], "justification":row[5], 
                "authoriser":row[6], "approved":row[7], "date_approved":row[8], 
                "rejected":row[9], "date_rejected":row[10], "executed":row[11], 
                "date_created":row[12], "date_modified":row[13]})
        return response

    @staticmethod
    def list_rolerequests_per_state(execution):
        stmt = text("SELECT Rolerequest.id, Rolerequest.request_type,"
        " Account.username, Wgroup.name, Role.name, Rolerequest.justification,"
        " Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved,"
        " Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed," 
        " Rolerequest.date_created, Rolerequest.date_modified"
        " FROM Rolerequest"
        " JOIN Account ON Rolerequest.account_id = Account.id "
        " JOIN Role ON Rolerequest.role_id = Role.id"
        " JOIN Wgroup ON Rolerequest.wgroup_id = Wgroup.id"
        " WHERE Rolerequest.executed = :execution"
        " ORDER BY Rolerequest.date_created").params(execution=execution)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "request_type":row[1], "user":row[2], 
                "wgroup":row[3], "role":row[4], "justification":row[5], 
                "authoriser":row[6], "approved":row[7], "date_approved":row[8], 
                "rejected":row[9], "date_rejected":row[10], "executed":row[11], 
                "date_created":row[12], "date_modified":row[13]})
        return response
              
    @staticmethod
    def list_rolerequests_my(user_id):
        stmt = text("SELECT Rolerequest.id, Rolerequest.request_type,"
        " Account.username, Wgroup.name, Role.name, Rolerequest.justification,"
        " Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved,"
        " Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed," 
        " Rolerequest.date_created, Rolerequest.date_modified"
        " FROM Rolerequest"
        " JOIN Account ON Rolerequest.account_id = Account.id "
        " JOIN Role ON Rolerequest.role_id = Role.id"
        " JOIN Wgroup ON Rolerequest.wgroup_id = Wgroup.id"
        " WHERE Rolerequest.account_id = :user_id"
        " ORDER BY Rolerequest.date_created").params(user_id=user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "request_type":row[1], "user":row[2], 
                "wgroup":row[3], "role":row[4], "justification":row[5], 
                "authoriser":row[6], "approved":row[7], "date_approved":row[8], 
                "rejected":row[9], "date_rejected":row[10], "executed":row[11], 
                "date_created":row[12], "date_modified":row[13]})
        return response