from flask_wtf import FlaskForm
from wtforms import SelectField
from application.wgroups.models import Wgroup
from application.roles.models import Role
from application.auth.models import User
from application import app, db


class MembershipForm(FlaskForm):
    account_id = SelectField("Käyttäjä", choices=[], coerce=int)
    wgroup_id = SelectField("Työryhmä", choices=[], coerce=int)
    role_id = SelectField("Rooli", choices=[], coerce=int)
   
    class Meta:
        csrf = False
