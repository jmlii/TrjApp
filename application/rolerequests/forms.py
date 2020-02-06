from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import RadioField, IntegerField, SelectField, StringField, validators
from application.wgroups.models import Wgroup
from application.roles.models import Role
from application.auth.models import User
from application import app, db


class RolerequestForm(FlaskForm):
    
    request_type = RadioField("Pyynnön tyyppi", 
        [validators.InputRequired()], choices=[('New', 'Uusi rooli'), 
        ('Modify', 'Muokkaus'), ('Remove', 'Poisto')])
    wgroup_id = IntegerField("Työryhmän id", [validators.InputRequired()])
    role_id = SelectField("Rooli", choices=[('1', 'Reader'), ('2', 'Editor'), ('3', 'Manager')], coerce=int)
    justification = StringField("Perustelut", [validators.Length(min=3)])

    class Meta:
        csrf = False



class RolerequestForm2(FlaskForm):
    
    request_type = RadioField("Pyynnön tyyppi", 
        [validators.InputRequired()], choices=[('New', 'Uusi rooli'), 
        ('Modify', 'Muokkaus'), ('Remove', 'Poisto')])
    account_id = IntegerField("Käyttäjän id", [validators.InputRequired()])
    wgroup_id = IntegerField("Työryhmän id", [validators.InputRequired()])
    role_id = SelectField("Rooli", choices=[('1', 'Reader'), ('2', 'Editor'), ('3', 'Manager')], coerce=int)
    justification = StringField("Perustelut", [validators.Length(min=3)])

    class Meta:
        csrf = False
