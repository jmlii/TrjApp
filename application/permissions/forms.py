from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PermissionForm(FlaskForm):
    name = StringField("Käyttäjätason nimi", [validators.Length(min=1, max=32)])

    class Meta:
        csrf = False