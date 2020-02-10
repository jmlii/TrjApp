from application import db

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    users = db.relationship("User", backref='permission', lazy=True)

    def __init__(self, name):
        self.name = name