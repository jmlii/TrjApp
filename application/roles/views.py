from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application import app, db, login_required
from application.roles.models import Role
from application.roles.forms import RoleForm
from application.userwgrouproles.models import Membership
from application.rolerequests.models import Rolerequest

# Roolien listaaminen
@app.route("/roles/", methods=["GET"])
@login_required(permission="admin")
def roles_index():
    return render_template("roles/list.html", roles = Role.query.all())

# Uuden roolin lisäämislomake
@app.route("/roles/new/")
@login_required(permission="admin")
def roles_form():
    return render_template("roles/new.html", form=RoleForm())

# Uuden roolin tallentaminen lomakkeelta tietokantaan
@app.route("/roles/", methods=["POST"])
@login_required(permission="admin")
def roles_create():
    form = RoleForm(request.form)

    if not form.validate():
        return render_template("roles/new.html", form=form)

    role = Role(form.name.data)

    db.session().add(role)
    db.session().commit()

    return redirect(url_for("roles_index"))

# Roolin poistaminen tietokannasta
@app.route("/roles/delete<role_id>/", methods=["POST"])
@login_required(permission="admin")
def roles_delete(role_id):
    role = Role.query.get(role_id)

    if Membership.query.filter_by(role_id=role.id).count() > 0 or Rolerequest.query.filter_by(role_id=role.id).count() > 0:
        return render_template("roles/list.html", roles = Role.query.all(), 
            error = "Et voi poistaa roolia, joka on liitettynä johonkin työryhmäjäsenyyteen tai hakemukseen.")
    
    db.session().delete(role)
    db.session().commit()

    return redirect(url_for("roles_index"))
