from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application import app, db
from application.roles.models import Role
from application.roles.forms import RoleForm

# Roolien listaaminen
@app.route("/roles/", methods=["GET"])
def roles_index():
    return render_template("roles/list.html", roles = Role.query.all())

# Uuden roolin lisäämislomake
@app.route("/roles/new/")
@login_required
def roles_form():
    return render_template("roles/new.html", form=RoleForm())

# Uuden roolin tallentaminen lomakkeelta tietokantaan
@app.route("/roles/", methods=["POST"])
@login_required
def roles_create():
    form = RoleForm(request.form)

    if not form.validate():
        return render_template("roles/new.html", form=form)

    r = Role(form.name.data)

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("roles_index"))

# Roolin poistaminen tietokannasta
@app.route("/roles/delete<role_id>/", methods=["POST"])
@login_required
def roles_delete(user_id):
    r = Role.query.get(role_id)
     
    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("roles_index"))