from application import db
from application.models import Base 
from sqlalchemy.sql import text

class Wgroup(Base):   
    name = db.Column(db.String(36), nullable=False)
    authoriser = db.Column(db.String(36), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    date_ended = db.Column(db.DateTime)

    rolerequests = db.relationship("Rolerequest", backref='wgroup', lazy=True)


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