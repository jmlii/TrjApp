# Tuodaan käyttöön Flask 
from flask import Flask
app = Flask(__name__)

# Tuodaan käyttöön SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Osoitetaan sovellus käyttämään Herokussa ollessa Herokun tietokantaa
import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
# Muulloin käytetään SQLite-tietokantaa nimeltä trj.db. 
# Tiedosto sijaitsee samassa kansiossa tämän sovelluksen tiedostojen kanssa.
else: 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trj.db"
    # Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Kirjautuminen
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään käyttääksesi tätä toimintoa."

# Käyttäjätason tunnistus
from functools import wraps

def login_required(_func=None, *, permission="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_permissions = set(("ANY", *current_user.permissions()))
            
            if permission not in acceptable_permissions:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)


# Ladataan sovelluksen sisältö
from application import views

from application.permissions import models
from application.permissions import views

from application.auth import models
from application.auth import views

from application.wgroups import models
from application.wgroups import views

from application.roles import models
from application.roles import views

from application.rolerequests import models
from application.rolerequests import views

from application.userwgrouproles import models
from application.userwgrouproles import views

# Kirjautumisen osa 2
from application.auth.models import User 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Luodaan tarvittavat tietokantataulut vain kerran
try:
    db.create_all()
except:
    pass

from application.permissions.models import Permission

try:
    if Permission.query.filter_by(name='admin').count()==0:
        db.session.add(Permission(name='admin'))
    if Permission.query.filter_by(name='basic').count()==0:
        db.session.add(Permission(name='basic'))
    if User.query.filter_by(username='adminadmin2').count()==0:
        adminuser = User(username='adminadmin')
        adminuser.first_name = 'Admin'
        adminuser.last_name = 'Admin'
        adminuser.password = '1q2w3e4r'
        adminuser.permission_id = Permission.query.from_self(Permission.id).filter_by(name='admin')
        db.session.add(adminuser)
    db.session.commit()
except:
    pass
    