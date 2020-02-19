from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, RadioField, BooleanField, validators

# kirjautumislomake
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False

# uuden käyttäjän lisääminen
class UserForm(FlaskForm):
    first_name = StringField("Etunimi", [validators.Length(min=1, max=64)])
    last_name = StringField("Sukunimi", [validators.Length(min=1, max=64)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=8, max=64)])
    password = PasswordField("Salasana", [validators.Length(min=6, max=64)])
    permission_id = RadioField("Käyttäjätaso", choices=[], coerce=int)

    class Meta:
        csrf = False

# käyttäjän tietojen muokkaaminen
class UserUpdateForm(FlaskForm):
    first_name = StringField("Etunimi", [validators.Length(min=1, max=64)])
    last_name = StringField("Sukunimi", [validators.Length(min=1, max=64)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=8, max=64)])
    permission_id = RadioField("Käyttäjätaso", choices=[], coerce=int)
    account_active = BooleanField("Käyttäjätunnus aktiivinen")

    class Meta:
        csrf = False

# Käyttäjän salasanan vaihtaminen
class UserUpdatePasswordForm(FlaskForm):
    password = PasswordField("Uusi salasana", [validators.Length(min=6, max=64)])
   
    class Meta:
        csrf = False   
