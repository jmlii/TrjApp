from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class WgroupForm(FlaskForm):
    name = StringField("Working group name", [validators.Length(min=3)])
    authoriser = StringField("Working group authoriser", [validators.InputRequired()])

    class Meta:
        csrf = False
