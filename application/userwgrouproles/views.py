from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db, login_required
from application.userwgrouproles.models import Membership
from application.userwgrouproles.forms import MembershipForm
from application.wgroups.models import Wgroup
from application.roles.models import Role
from application.auth.models import User

# Jäsenyyksien listaaminen
@app.route("/memberships/", methods=["GET"])
@login_required(permission="admin")
def memberships_index():
    return render_template("userwgrouproles/list.html", memberships = Membership.list_memberships())
   
# Uuden jäsenyyden lisääminen
@app.route("/memberships/new/")
@login_required(permission="admin")
def memberships_form():
    form = MembershipForm()
    form.account_id.choices = [(user.id, user.username) for user in User.query.filter_by(account_active=True).order_by("username")]
    form.wgroup_id.choices = [(wgroup.id, wgroup.name) for wgroup in Wgroup.query.filter_by(active=True).order_by("name")]
    form.role_id.choices = [(role.id, role.name) for role in Role.query.all()]
    return render_template("userwgrouproles/new.html", form=form)
   
# Uuden jäsenyyden tallentaminen lomakkeelta tietokantaan
@app.route("/memberships", methods=["POST"])
@login_required(permission="admin")
def memberships_create():
    form = MembershipForm(request.form)
    form.account_id.choices = [(user.id, user.username) for user in User.query.filter_by(account_active=True).order_by("username")]
    form.wgroup_id.choices = [(wgroup.id, wgroup.name) for wgroup in Wgroup.query.filter_by(active=True).order_by("name")]
    form.role_id.choices = [(role.id, role.name) for role in Role.query.all()]
    
    if not form.validate():
        return render_template("userwgrouproles/new.html", form=form)

    membership = Membership(form.account_id.data, form.wgroup_id.data, form.role_id.data)

    if Membership.query.filter_by(account_id=form.account_id.data, wgroup_id=form.wgroup_id.data, role_id=form.role_id.data, date_ended=None).count() > 0:
        return render_template("userwgrouproles/new.html", form=form, error = "Tämä jäsenyys on jo olemassa. Tarkista valinnat.")
    
    db.session().add(membership)
    db.session().commit()

    return redirect(url_for("memberships_index"))

# Jäsenyyden lopettaminen
@app.route("/memberships/end<account_id>-<wgroup_id>-<role_id>/", methods=["POST"])
@login_required(permission="admin")
def memberships_end(account_id, wgroup_id, role_id):
    
    membership = Membership.query.filter_by(account_id=account_id, wgroup_id=wgroup_id, role_id=role_id).first()
    membership.date_ended = db.func.current_timestamp()

    db.session().commit()

    return redirect(url_for("memberships_index"))

