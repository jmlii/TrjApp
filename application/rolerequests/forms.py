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
    
    wgroups = Wgroup.query.order_by(Wgroup.name)
    wgroup_choices = []
    for wgroup in wgroups:
        wgroup_choices.append((wgroup.id, wgroup.name))
    wgroup_id = SelectField("Työryhmä", choices=wgroup_choices, coerce=int)
    
    roles = Role.query.all()
    role_choices = []
    for role in roles:
        role_choices.append((role.id, role.name))
    role_id = SelectField("Rooli", choices=role_choices, coerce=int)

    justification = StringField("Perustelut", [validators.Length(min=3)])

    class Meta:
        csrf = False



class RolerequestForm2(FlaskForm):
    
    request_type = RadioField("Pyynnön tyyppi", 
        [validators.InputRequired()], choices=[('New', 'Uusi rooli'), 
        ('Modify', 'Muokkaus'), ('Remove', 'Poisto')])
    
    accounts = User.query.order_by(User.username)
    account_choices = []
    for account in accounts:
        account_choices.append((account.id, account.username))

    account_id = SelectField("Käyttäjä", choices=account_choices, coerce=int)
    
    wgroups = Wgroup.query.order_by(Wgroup.name)
    wgroup_choices = []
    for wgroup in wgroups:
        wgroup_choices.append((wgroup.id, wgroup.name))
    wgroup_id = SelectField("Työryhmä", choices=wgroup_choices, coerce=int)
    
    roles = Role.query.all()
    role_choices = []
    for role in roles:
        role_choices.append((role.id, role.name))
    role_id = SelectField("Rooli", choices=role_choices, coerce=int)

    justification = StringField("Perustelut", [validators.Length(min=3)])

    class Meta:
        csrf = False
