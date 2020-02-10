from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm


# Käyttäjien sisäänkirjautuminen
@app.route("/auth/login/", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user or user.account_active == False:
        return render_template("auth/loginform.html", form = form, error = "Virheellinen käyttäjätunnus tai salasana.")

    login_user(user)
    return redirect(url_for("index"))    

# Käyttäjän uloskirjautuminen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


# Käyttäjien listaaminen
@app.route("/users/", methods=["GET"])
@login_required()
def users_index():
    return render_template("auth/list.html", users = User.query.all())

# Uuden käyttäjän luominen
@app.route("/users/new/")
@login_required(permission="2")
def users_form():
    return render_template("/auth/new.html", form = UserForm())

# Luodun käyttäjän tiedot tietokantaan
@app.route("/users/", methods=["POST"])
@login_required(permission="2")
def users_create():
    form = UserForm(request.form)
    
    if not form.validate():
        return render_template("auth/new.html", form=form)

    user = User(form.username.data)
    user.first_name = form.first_name.data
    user.last_name = form.last_name.data
    user.password = form.password.data
    user.permission_id = form.permission_id.data

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("users_index"))
    
# Käyttäjän asettaminen lepotilaan
@app.route("/users/inactivate<user_id>/", methods=["POST"])
@login_required(permission="2")
def users_inactivate(user_id):
    user = User.query.get(user_id)
    user.account_active = False
    user.date_inactivated = db.func.current_timestamp()
    db.session().commit()

    return redirect(url_for("users_index"))

# Käyttäjän poistaminen tietokannasta
@app.route("/users/delete<user_id>/", methods=["POST"])
@login_required(permission="2")
def users_delete(user_id):
    user = User.query.get(user_id)
     
    db.session().delete(user)
    db.session().commit()

    return redirect(url_for("users_index"))
