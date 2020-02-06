from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db
from application.rolerequests.models import Rolerequest
from application.rolerequests.forms import RolerequestForm, RolerequestForm2

# Pyyntöjen listaaminen
@app.route("/rolerequests/", methods=["GET"])
def rolerequests_index():
    return render_template("rolerequests/list.html", rolerequests = Rolerequest.query.all())


# Uuden roolipyynnön itselle lähettäminen
@app.route("/rolerequests/new/")
@login_required
def rolerequests_form():
    return render_template("rolerequests/new.html", form=RolerequestForm())

# Uuden roolipyynnön itselle tallentaminen lomakkeelta tietokantaan
@app.route("/rolerequests/", methods=["POST"])
@login_required
def rolerequests_create():
    form = RolerequestForm(request.form)

    if not form.validate():
        return render_template("rolerequests/new.html", form=form)

    rolerequest = Rolerequest(form.request_type.data)
    rolerequest.account_id = current_user.id
    rolerequest.role_id = form.role_id.data
    rolerequest.wgroup_id = form.wgroup_id.data
    rolerequest.justification = form.justification.data

    db.session().add(rolerequest)
    db.session().commit()

    return redirect(url_for("rolerequests_index"))

# Uuden roolipyynnön toiselle käyttäjälle lähettäminen
@app.route("/rolerequests/new2/")
@login_required
def rolerequests_form2():
    return render_template("rolerequests/new2.html", form=RolerequestForm2())

# Uuden roolipyynnön toiselle käyttäjälle tallentaminen lomakkeelta tietokantaan
@app.route("/rolerequests/2", methods=["POST"])
@login_required
def rolerequests_create2():
    form = RolerequestForm2(request.form)

    if not form.validate():
        return render_template("rolerequests/new2.html", form=form)

    rolerequest2 = Rolerequest(form.request_type.data)
    rolerequest2.account_id = form.account_id.data
    rolerequest2.role_id = form.role_id.data
    rolerequest2.wgroup_id = form.wgroup_id.data
    rolerequest2.justification = form.justification.data

    db.session().add(rolerequest2)
    db.session().commit()

    return redirect(url_for("rolerequests_index"))

# Roolipyynnön hyväksyminen
@app.route("/rolerequests/approve<rolerequest_id>/", methods=["POST"])
@login_required
def rolerequests_approve(user_id):
    rolerequest = Rolerequest.query.get(rolerequest_id)
    rolerequest.approved = True
    rolerequest.date_approved = db.func.current_timestamp()

    db.session().commit()

    return redirect(url_for("rolerequests_index"))


# Roolipyynnön hylkääminen
@app.route("/rolerequests/reject<rolerequest_id>/", methods=["POST"])
@login_required
def rolerequests_reject(user_id):
    rolerequest = Rolerequest.query.get(rolerequest_id)
    rolerequest.rejected = True
    rolerequest.date_rejected = db.func.current_timestamp()
     
    db.session().commit()

    return redirect(url_for("rolerequests_index"))


# Roolipyynnön merkitseminen toteutetuksi
@app.route("/rolerequests/set_executed<rolerequest_id>/", methods=["POST"])
@login_required
def rolerequests_set_executed(user_id):
    rolerequest = Rolerequest.query.get(rolerequest_id)
    rolerequest.executed = True     

    db.session().commit()

    return redirect(url_for("rolerequests_index"))