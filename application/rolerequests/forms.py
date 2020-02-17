from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import RadioField, SelectField, StringField, validators
from application.wgroups.models import Wgroup
from application.roles.models import Role
from application.auth.models import User
from application import app, db

class RolerequestForm(FlaskForm):
    request_type = RadioField("Pyynnön tyyppi", 
        [validators.InputRequired()], choices=[('New', 'Uusi rooli'), 
        ('Modify', 'Muokkaus'), ('Remove', 'Poisto')])
    wgroup_id = SelectField("Työryhmä", choices=[], coerce=int)
    role_id = SelectField("Rooli", choices=[], coerce=int)
    justification = StringField("Perustelut", [validators.Length(min=3)])

    class Meta:
        csrf = False

class RolerequestForm2(FlaskForm):
    request_type = RadioField("Pyynnön tyyppi", 
        [validators.InputRequired()], choices=[('New', 'Uusi rooli'), 
        ('Modify', 'Muokkaus'), ('Remove', 'Poisto')])
    account_id = SelectField("Käyttäjä", choices=[], coerce=int)
    wgroup_id = SelectField("Työryhmä", choices=[], coerce=int)
    role_id = SelectField("Rooli", choices=[], coerce=int)
    justification = StringField("Perustelut", [validators.Length(min=3)])

    class Meta:
        csrf = False
