from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class WgroupForm(FlaskForm):
    name = StringField("Työryhmän nimi", [validators.Length(min=3)])
    authoriser = StringField("Työryhmän oikeushyväksyjä", [validators.InputRequired()])

    class Meta:
        csrf = False

class WgroupUpdateForm(FlaskForm):
    name = StringField("Työryhmän nimi", [validators.Length(min=3)])
    authoriser = StringField("Työryhmän oikeushyväksyjä", [validators.InputRequired()])
    active = BooleanField("Työryhmä aktiivinen")

    class Meta:
        csrf = False
