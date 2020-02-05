from application import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    rolerequests = db.relationship("Rolerequest", backref='role', lazy=True)

    def __init__(self, name):
        self.name = name