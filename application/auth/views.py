from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm, UserUpdateForm, UserUpdatePasswordForm
from application.permissions.models import Permission

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
    page=request.args.get('page', 1, type=int)
    users = User.query.order_by("last_name").paginate(page=page, per_page=10, error_out=False)

    return render_template("auth/list.html", users=users)

# Uuden käyttäjän luominen
@app.route("/users/new/")
@login_required(permission="admin")
def users_form():
    form = UserForm()
    form.permission_id.choices = [(permission.id, permission.name) for permission in Permission.query.all()]
    return render_template("/auth/new.html", form = form)

# Luodun käyttäjän tiedot tietokantaan
@app.route("/users/", methods=["POST"])
@login_required(permission="admin")
def users_create():
    form = UserForm(request.form)
    form.permission_id.choices = [(permission.id, permission.name) for permission in Permission.query.all()]
    
    if not form.validate():
        return render_template("auth/new.html", form=form)

    user = User(form.username.data)
    user.first_name = form.first_name.data
    user.last_name = form.last_name.data
    user.password = form.password.data
    user.permission_id = form.permission_id.data
    if User.query.filter_by(username=form.username.data).count() > 0:
        return render_template("auth/new.html", form=form, error = "Tunnus on jo käytössä. Valitse uusi käyttäjätunnus.")
    
    db.session().add(user)
    db.session().commit()

    return redirect(url_for("users_index"))
    
# Käyttäjän asettaminen lepotilaan
@app.route("/users/inactivate<user_id>/", methods=["POST"])
@login_required(permission="admin")
def users_inactivate(user_id):
    user = User.query.get(user_id)
    user.account_active = False
    user.date_inactivated = db.func.current_timestamp()
    db.session().commit()
    return redirect(url_for("users_index"))

# Käyttäjän poistaminen tietokannasta
@app.route("/users/delete<user_id>/", methods=["POST"])
@login_required(permission="admin")
def users_delete(user_id):
    user = User.query.get(user_id)
    db.session().delete(user)
    db.session().commit()
    return redirect(url_for("users_index"))

# Käyttäjän perustietojen muokkaaminen
@app.route("/users/update<user_id>/", methods=["GET", "POST"])
@login_required(permission="admin")
def users_update(user_id):
    user = User.query.get(user_id)
    form = UserUpdateForm(request.form)
    form.permission_id.choices = [(permission.id, permission.name) for permission in Permission.query.all()]
    
    account_active_old = user.account_active

    if request.method=="POST" and form.validate():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.username = form.username.data
        user.permission_id = form.permission_id.data
        user.account_active = form.account_active.data
        
        if account_active_old != user.account_active and user.account_active == False:
            user.date_inactivated = db.func.current_timestamp()
        if account_active_old != user.account_active and user.account_active == True:
            user.date_inactivated = None

        if User.query.filter_by(username=form.username.data).first() is not user:
            return render_template("auth/update.html", form=form, error = "Tunnus on jo käytössä. Valitse uusi käyttäjätunnus.")
    
        db.session().commit()
        return redirect(url_for("users_index"))

    form.first_name.data = user.first_name
    form.last_name.data = user.last_name
    form.username.data = user.username
    form.permission_id.data = user.permission_id
    form.account_active.data = user.account_active
    
    return render_template("auth/update.html", user=user, user_id=user_id, form=form)      

# Käyttäjän salasanan vaihtaminen
@app.route("/users/update/password<user_id>/", methods=["GET", "POST"])
@login_required(permission="admin")
def users_updatepassword(user_id):
    user = User.query.get(user_id)
    form = UserUpdatePasswordForm(request.form)

    if request.method=="POST" and form.validate():
        user.password = form.password.data    
        db.session().commit()
        return redirect(url_for("users_index"))

    return render_template("auth/updatepassword.html", user=user, user_id=user_id, form=form)

# Käyttäjän voimassaolevien työryhmäjäsenyyksien listaaminen
@app.route("/users/memberships<user_id>/", methods=["GET"])
@login_required
def users_memberships(user_id):
    user = User.query.get(user_id)
    
    if current_user.permission_name() != "admin":
        if not user or user.account_active == False:
            return render_template("auth/listmemberships.html", error = "Käyttäjää ei löydy tai käyttäjä ei ole aktiivinen.")
    
    if current_user.permission_name() == "admin":
        if not user:
            return render_template("auth/listmemberships.html", error = "Käyttäjää ei löydy.")

    return render_template("auth/listmemberships.html", user=user, 
    list_memberships = User.list_memberships(user_id))

# Kirjautuneen käyttäjän omien voimassaolevien työryhmäjäsenyyksien listaaminen
@app.route("/users/memberships/my/", methods=["GET"])
@login_required
def my_memberships():
    user = current_user
    return render_template("auth/listmemberships.html", user=user, 
    list_memberships = User.list_memberships(current_user.id))
