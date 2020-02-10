from flask_wtf import FlaskForm
from wtforms import StringField

class PermissionForm(FlaskForm):
    name = StringField("Käyttäjätason nimi")

    class Meta:
        csrf = False