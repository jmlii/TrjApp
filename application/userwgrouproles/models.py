from application import db

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
