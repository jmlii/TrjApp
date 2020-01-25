from application import app, db
from flask import redirect, render_template, request, url_for
from application.wgroups.models import Wgroup

@app.route("/wgroups/", methods=["GET"])
def wgroups_index():
    return render_template("wgroups/list.html", wgroups = Wgroup.query.all())

@app.route("/wgroups/new/")
def wgroups_form():
    return render_template("wgroups/new.html")

@app.route("/wgroups/created/", methods=["POST"])
def wgroups_create():
    wg = Wgroup(request.form.get("name"), 
    request.form.get("authoriser"))

    db.session().add(wg)
    db.session().commit()

    return "Tietokantaan lisätty uusi työryhmä: Työryhmän nimi " + \
    wg.name + ", hyväksyjä " + wg.authoriser

@app.route("/wgroups/end<wgroup_id>/", methods=["POST"])
def wgroups_set_end(wgroup_id):
    wg = Wgroup.query.get(wgroup_id)
    wg.active = False
    db.session().commit()

    return redirect(url_for("wgroups_index"))
