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

    rr = Rolerequest(form.request_type.data, form.justification.data)
    rr.account_id = current_user.id
    rr.role_id = form.role_id.data
    rr.wgroup_id = form.wgroup_id.data

    db.session().add(rr)
    db.session().commit()

    return redirect(url_for("rolerequests_index"))

# Uuden roolipyynnön toiselle käyttäjälle lähettäminen
@app.route("/rolerequests/new2/")
@login_required
def rolerequests_form2():
    return render_template("rolerequests/new2.html", form=RolerequestForm2())

# Uuden roolipyynnön toiselle käyttäjälle tallentaminen lomakkeelta tietokantaan
@app.route("/rolerequests/", methods=["POST"])
@login_required
def rolerequests_create2():
    form = RolerequestForm2(request.form)

    if not form.validate():
        return render_template("rolerequests/new.html", form=form)

    rr = Rolerequest(form.request_type.data, form.justification.data)
    rr.account_id = form.account_id.data
    rr.role_id = form.role_id.data
    rr.wgroup_id = form.wgroup_id.data

    db.session().add(rr)
    db.session().commit()

    return redirect(url_for("rolerequests_index"))

# Roolipyynnön hyväksyminen
@app.route("/rolerequests/approve<rolerequest_id>/", methods=["POST"])
@login_required
def rolerequests_approve(user_id):
    rr = Rolerequest.query.get(rolerequest_id)
    rr.approved = True
    rr.date_approved = db.func.current_timestamp()

    db.session().commit()

    return redirect(url_for("rolerequests_index"))


# Roolipyynnön hylkääminen
@app.route("/rolerequests/reject<rolerequest_id>/", methods=["POST"])
@login_required
def rolerequests_reject(user_id):
    rr = Rolerequest.query.get(rolerequest_id)
    rr.rejected = True
    rr.date_rejected = db.func.current_timestamp()
     
    db.session().commit()

    return redirect(url_for("rolerequests_index"))


# Roolipyynnön merkitseminen toteutetuksi
@app.route("/rolerequests/set_executed<rolerequest_id>/", methods=["POST"])
@login_required
def rolerequests_set_executed(user_id):
    rr = Rolerequest.query.get(rolerequest_id)
    rr.executed = True     

    db.session().commit()

    return redirect(url_for("rolerequests_index"))