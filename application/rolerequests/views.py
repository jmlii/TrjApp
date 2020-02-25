from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db, login_required
from application.rolerequests.models import Rolerequest
from application.rolerequests.forms import RolerequestForm, RolerequestForm2
from application.wgroups.models import Wgroup
from application.roles.models import Role
from application.auth.models import User

# Jäsenyyspyyntöjen listaaminen
@app.route("/rolerequests/", methods=["GET"])
@login_required(permission="admin")
def rolerequests_index():
    page=request.args.get('page', 1, type=int)
    rolerequests= Rolerequest.query.from_self(Rolerequest.id, Rolerequest.request_type, \
        User.username.label('user'), Wgroup.name.label('wgroup'), Role.name.label('role'), \
        Rolerequest.justification, Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved, \
        Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed, \
        Rolerequest.date_created, Rolerequest.date_modified).\
        join(User, Rolerequest.account_id == User.id).\
        join(Wgroup, Rolerequest.wgroup_id == Wgroup.id).\
        join(Role, Rolerequest.role_id == Role.id).\
        order_by(Rolerequest.date_created.desc()).\
        paginate(page=page, per_page=10, error_out=False)
    
    return render_template("rolerequests/list.html", 
        rolerequests = rolerequests)

# Avoimien jäsenyyspyyntöjen listaaminen
@app.route("/rolerequests/open", methods=["GET"])
@login_required(permission="admin")
def rolerequests_index_open():
    page=request.args.get('page', 1, type=int)
    rolerequests= Rolerequest.query.from_self(Rolerequest.id, Rolerequest.request_type, \
        User.username.label('user'), Wgroup.name.label('wgroup'), Role.name.label('role'), \
        Rolerequest.justification, Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved, \
        Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed, \
        Rolerequest.date_created, Rolerequest.date_modified).\
        join(User, Rolerequest.account_id == User.id).\
        join(Wgroup, Rolerequest.wgroup_id == Wgroup.id).\
        join(Role, Rolerequest.role_id == Role.id).\
        filter(Rolerequest.executed==False).\
        order_by(Rolerequest.date_created).\
        paginate(page=page, per_page=10, error_out=False)
    
    return render_template("rolerequests/list_open.html", 
        rolerequests = rolerequests)

# Suljettujen jäsenyyspyyntöjen listaaminen
@app.route("/rolerequests/closed", methods=["GET"])
@login_required(permission="admin")
def rolerequests_index_closed():
    page=request.args.get('page', 1, type=int)
    rolerequests= Rolerequest.query.from_self(Rolerequest.id, Rolerequest.request_type, \
        User.username.label('user'), Wgroup.name.label('wgroup'), Role.name.label('role'), \
        Rolerequest.justification, Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved, \
        Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed, \
        Rolerequest.date_created, Rolerequest.date_modified).\
        join(User, Rolerequest.account_id == User.id).\
        join(Wgroup, Rolerequest.wgroup_id == Wgroup.id).\
        join(Role, Rolerequest.role_id == Role.id).\
        filter(Rolerequest.executed==True).\
        order_by(Rolerequest.date_created.desc()).\
        paginate(page=page, per_page=10, error_out=False)

    return render_template("rolerequests/list_closed.html", 
        rolerequests = rolerequests)

# Omien jäsenyyspyyntöjen listaaminen
@app.route("/rolerequests/my/", methods=["GET"])
@login_required
def rolerequests_my_index():  
    current_user_id = current_user.id 
    page=request.args.get('page', 1, type=int)
    rolerequests= Rolerequest.query.from_self(Rolerequest.id, Rolerequest.request_type, \
        User.username.label('user'), Wgroup.name.label('wgroup'), Role.name.label('role'), \
        Rolerequest.justification, Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved, \
        Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed, \
        Rolerequest.date_created, Rolerequest.date_modified).\
        join(User, Rolerequest.account_id == User.id).\
        join(Wgroup, Rolerequest.wgroup_id == Wgroup.id).\
        join(Role, Rolerequest.role_id == Role.id).\
        filter(Rolerequest.account_id == current_user_id).\
        order_by(Rolerequest.date_created.desc()).\
        paginate(page=page, per_page=10, error_out=False)
    
    return render_template("rolerequests/list.html", 
        rolerequests = rolerequests, request_list = "my_requests")

# Uuden jäsenyyspyynnön itselle lähettäminen
@app.route("/rolerequests/new/")
@login_required
def rolerequests_form():
    form = RolerequestForm()
    form.wgroup_id.choices = [(wgroup.id, wgroup.name) for wgroup in Wgroup.query.filter_by(active=True).order_by("name")]
    form.role_id.choices = [(role.id, role.name) for role in Role.query.all()]
    return render_template("rolerequests/new.html", form=form)

# Uuden jäsenyyspyynnön itselle tallentaminen lomakkeelta tietokantaan
@app.route("/rolerequests/", methods=["POST"])
@login_required
def rolerequests_create():
    form = RolerequestForm()
    form.wgroup_id.choices = [(wgroup.id, wgroup.name) for wgroup in Wgroup.query.filter_by(active=True).order_by("name")]
    form.role_id.choices = [(role.id, role.name) for role in Role.query.all()]

    if not form.validate():
        return render_template("rolerequests/new.html", form=form)

    rolerequest = Rolerequest(form.request_type.data)
    rolerequest.account_id = current_user.id
    rolerequest.wgroup_id = form.wgroup_id.data
    rolerequest.role_id = form.role_id.data
    rolerequest.justification = form.justification.data

    db.session().add(rolerequest)
    db.session().commit()
    return redirect(url_for("rolerequests_my_index"))

# Uuden jäsenyyspyynnön toiselle käyttäjälle lähettäminen
@app.route("/rolerequests/new2/")
@login_required(permission="admin")
def rolerequests_form2():
    form = RolerequestForm2()
    form.account_id.choices = [(user.id, user.username) for user in User.query.filter_by(account_active=True).order_by("username")]
    form.wgroup_id.choices = [(wgroup.id, wgroup.name) for wgroup in Wgroup.query.filter_by(active=True).order_by("name")]
    form.role_id.choices = [(role.id, role.name) for role in Role.query.all()]
    return render_template("rolerequests/new2.html", form=form)
   
# Uuden jäsenyyspyynnön toiselle käyttäjälle tallentaminen lomakkeelta tietokantaan
@app.route("/rolerequests/2", methods=["POST"])
@login_required(permission="admin")
def rolerequests_create2():
    form = RolerequestForm2(request.form)
    form.account_id.choices = [(user.id, user.username) for user in User.query.filter_by(account_active=True).order_by("username")]
    form.wgroup_id.choices = [(wgroup.id, wgroup.name) for wgroup in Wgroup.query.filter_by(active=True).order_by("name")]
    form.role_id.choices = [(role.id, role.name) for role in Role.query.all()]
    
    if not form.validate():
        return render_template("rolerequests/new2.html", form=form)

    rolerequest2 = Rolerequest(form.request_type.data)
    rolerequest2.account_id = form.account_id.data
    rolerequest2.wgroup_id = form.wgroup_id.data
    rolerequest2.role_id = form.role_id.data
    rolerequest2.justification = form.justification.data

    db.session().add(rolerequest2)
    db.session().commit() 
    return redirect(url_for("rolerequests_index_open"))

# Jäsenyyspyynnön hyväksyminen
@app.route("/rolerequests/approve<rolerequest_id>/", methods=["POST"])
@login_required(permission="admin")
def rolerequests_approve(rolerequest_id):
    rolerequest = Rolerequest.query.get(rolerequest_id)
    rolerequest.approved = True
    rolerequest.date_approved = db.func.current_timestamp()

    db.session().commit()
    return redirect(url_for("rolerequests_index_open"))

# Jäsenyyspyynnön hylkääminen
@app.route("/rolerequests/reject<rolerequest_id>/", methods=["POST"])
@login_required(permission="admin")
def rolerequests_reject(rolerequest_id):
    rolerequest = Rolerequest.query.get(rolerequest_id)
    rolerequest.rejected = True
    rolerequest.date_rejected = db.func.current_timestamp()
    rolerequest.executed = True 

    db.session().commit()
    return redirect(url_for("rolerequests_index_closed"))

# Jäsenyyspyynnön merkitseminen toteutetuksi
@app.route("/rolerequests/set_executed<rolerequest_id>/", methods=["POST"])
@login_required(permission="admin")
def rolerequests_set_executed(rolerequest_id):
    rolerequest = Rolerequest.query.get(rolerequest_id)
    rolerequest.executed = True 

    db.session().commit()
    return redirect(url_for("rolerequests_index_closed"))

# Jäsenyyspyynnön perustietojen muokkaaminen
@app.route("/rolerequests/update<rolerequest_id>/", methods=["GET", "POST"])
@login_required(permission="admin")
def rolerequests_update(rolerequest_id):
    
    rolerequest = Rolerequest.query.get(rolerequest_id)
    form = RolerequestForm2(request.form)
    form.account_id.choices = [(user.id, user.username) for user in User.query.filter_by(account_active=True).order_by("username")]
    form.wgroup_id.choices = [(wgroup.id, wgroup.name) for wgroup in Wgroup.query.filter_by(active=True).order_by("name")]
    form.role_id.choices = [(role.id, role.name) for role in Role.query.all()]
    
    if request.method=="POST" and form.validate():

        rolerequest = Rolerequest(form.request_type.data)
        rolerequest.account_id = form.account_id.data
        rolerequest.wgroup_id = form.wgroup_id.data
        rolerequest.role_id = form.role_id.data
        rolerequest.justification = form.justification.data

        db.session.commit()
        return redirect(url_for("rolerequests_index"))

    form.request_type.data = rolerequest.request_type
    form.account_id.data = rolerequest.account_id 
    form.wgroup_id.data = rolerequest.wgroup_id 
    form.role_id.data = rolerequest.role_id 
    form.justification.data = rolerequest.justification 

    return render_template("rolerequests/update.html", rolerequest=rolerequest, rolerequest_id=rolerequest_id, form=form)      

# Jäsenyyspyynnön poistaminen tietokannasta
@app.route("/rolerequests_delete<rolerequest_id>/", methods=["POST"])
@login_required(permission="admin")
def rolerequests_delete(rolerequest_id):
    rolerequest = Rolerequest.query.get(rolerequest_id)
    db.session().delete(rolerequest)

    db.session().commit()
    return redirect(url_for("rolerequests_index_open"))
