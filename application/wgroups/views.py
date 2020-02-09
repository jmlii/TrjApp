from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application import app, db
from application.wgroups.models import Wgroup
from application.wgroups.forms import WgroupForm, WgroupUpdateForm

@app.route("/wgroups/", methods=["GET"])
def wgroups_index():
    return render_template("wgroups/list.html", 
        wgroups = Wgroup.query.all(), 
        count_new_rolerequests = Wgroup.count_rolerequests_per_wgroup(False, False, False),
        count_approved_rolerequests = Wgroup.count_rolerequests_per_wgroup(True, False, False))

@app.route("/wgroups/new/")
@login_required
def wgroups_form():
    return render_template("wgroups/new.html", form = WgroupForm())

@app.route("/wgroups/", methods=["POST"])
@login_required
def wgroups_create():
    form = WgroupForm(request.form)

    if not form.validate():
        return render_template("wgroups/new.html", form=form)

    wgroup = Wgroup(form.name.data)
    wgroup.authoriser = form.authoriser.data

    db.session().add(wgroup)
    db.session().commit()

    return redirect(url_for("wgroups_index"))

@app.route("/wgroups/end<wgroup_id>/", methods=["POST"])
@login_required
def wgroups_set_end(wgroup_id):
    wgroup = Wgroup.query.get(wgroup_id)
    wgroup.active = False
    wgroup.date_ended = db.func.current_timestamp()
    db.session().commit()

    return redirect(url_for("wgroups_index"))

@app.route("/wgroups/update<wgroup_id>/", methods=["GET", "POST"])
@login_required
def wgroups_update(wgroup_id):
    
    wgroup = Wgroup.query.get(wgroup_id)
    form = WgroupUpdateForm(request.form)

    active_old = wgroup.active

    if request.method=="POST" and form.validate():
        wgroup.name = form.name.data
        wgroup.authoriser = form.authoriser.data
        wgroup.active = form.active.data
        if active_old != wgroup.active and wgroup.active == False:
            wgroup.date_ended = db.func.current_timestamp()
        if active_old != wgroup.active and wgroup.active == True:
            wgroup.date_ended = None

        db.session.commit()

        return redirect(url_for("wgroups_index"))

    form.name.data = wgroup.name
    form.authoriser.data = wgroup.authoriser
    form.active.data = wgroup.active

    return render_template("wgroups/update.html", wgroup_id=wgroup_id, form=form)      
