from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application import app, db, login_required
from application.permissions.models import Permission
from application.permissions.forms import PermissionForm

# Käyttäjätasojen listaaminen
@app.route("/permissions/", methods=["GET"])
@login_required(permission="admin")
def permissions_index():
    return render_template("permissions/list.html", 
    permissions = Permission.query.all())

# Uuden käyttäjätason lisäämislomake
@app.route("/permissions/new/")
@login_required(permission="admin")
def permissions_form():
    return render_template("permissions/new.html", form=PermissionForm())

# Uuden käyttäjätason tallentaminen lomakkeelta tietokantaan
@app.route("/permissions/", methods=["POST"])
@login_required(permission="admin")
def permissions_create():
    form = PermissionForm(request.form)

    if not form.validate():
        return render_template("permissions/new.html", form=form)

    permission = Permission(form.name.data)

    db.session().add(permission)
    db.session().commit()

    return redirect(url_for("permissions_index"))

# Käyttäjätason poistaminen tietokannasta
@app.route("/permissions/delete<permission_id>/", methods=["POST"])
@login_required(permission="admin")
def permissions_delete(permission_id):
    permission = Permission.query.get(permission_id)

    if permission.users:
        return render_template("permissions/list.html", permissions = Permission.query.all(), 
            error = "Et voi poistaa käyttäjätasoa, joka on käytössä jollain käyttäjällä.")

    db.session().delete(permission)
    db.session().commit()

    return redirect(url_for("permissions_index"))
    