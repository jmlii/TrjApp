from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

# kirjautumislomake
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

# uuden käyttäjän lisääminen
class UserForm(FlaskForm):
    first_name = StringField("First name", [validators.Length(min=1)])
    last_name = StringField("Last name", [validators.Length(min=1)])
    username = StringField("Username", [validators.Length(min=8)])
    password = PasswordField("Password")

    class Meta:
        csrf = False