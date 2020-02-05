from flask_wtf import FlaskForm
from wtforms import StringField

class RoleForm(FlaskForm):
    name = StringField("Roolin nimi")

    class Meta:
        csrf = False