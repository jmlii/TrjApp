from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application import app, db
from application.wgroups.models import Wgroup
from application.wgroups.forms import WgroupForm

@app.route("/wgroups/", methods=["GET"])
def wgroups_index():
    return render_template("wgroups/list.html", wgroups = Wgroup.query.all())

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
    wg = Wgroup.query.get(wgroup_id)
    wg.active = False
    wg.date_ended = db.func.current_timestamp()
    db.session().commit()

    return redirect(url_for("wgroups_index"))
