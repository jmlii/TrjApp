from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, RadioField, validators

# kirjautumislomake
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False

# uuden käyttäjän lisääminen
class UserForm(FlaskForm):
    first_name = StringField("Etunimi", [validators.Length(min=1)])
    last_name = StringField("Sukunimi", [validators.Length(min=1)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=8)])
    password = PasswordField("Salasana", [validators.Length(min=6)])
    permission_id = RadioField("Käyttäjätaso", [validators.InputRequired()], choices=[('1', 'Peruskäyttäjä'), ('2', 'Pääkäyttäjä')])

    class Meta:
        csrf = False