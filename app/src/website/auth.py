from flask import Blueprint, render_template, request, flash, redirect, url_for, escape, session
from .models import Servers
from . import db
from datetime import datetime
from .functions import fast_ping
from functools import wraps
auth = Blueprint('auth', __name__)


# View decorator that redirects anonymous users to the login page.
def login_required(f):
    @wraps(f)
    def warp(*args,  **kwargs):
        if "logged_in" in session:
            return f(*args,  **kwargs)
        else:
            return redirect(url_for("auth.login"))
    return warp


# Log in user by adding the user id to the session.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "Username" and password == "Password":
            session['logged_in'] = username
            return redirect(url_for("views.home"))

        if username != "Username":
            flash("שם משתמש שגוי", category="incorrect_username")

        if password != "Password":
            flash("סיסמא שגויה", category="incorrect_password")

        return redirect(url_for("auth.login"))

    return render_template("login.html")


# Pinger to check servers IP status and displaying the results in a table with options to remote access, delete, edit and add server.
@auth.route('/servers', methods=['POST', 'GET'])
@login_required
def servers():
    if request.method == 'POST':
        ip = request.form.get("ip")
        name = request.form.get("name")

        new_server = Servers(ip=ip, name=name, status=fast_ping(ip))

        try:
            db.session.add(new_server)
            db.session.commit()
            return redirect("/servers")

        except:
            return "There was an error adding your server"


    servers = Servers.query.order_by(Servers.id)
    return render_template('servers.html', servers=servers)


# Edit Server parameters.
@auth.route('/servers/edit/<int:server_id>', methods=['POST', 'GET'])
@login_required
def edit(server_id):
    edited_server = Servers.query.get_or_404(server_id)

    if request.method == 'POST':
        edited_server.ip = request.form.get("ip")
        edited_server.status = fast_ping(edited_server.ip)
        edited_server.status_date = datetime.now()
        edited_server.name = request.form.get("name")

        try:
            db.session.commit()
            return redirect("/servers")
        except:
            return "There was a problem to update the server"

    return render_template("edit.html", edited_server=edited_server)


# Delete Server from the DB table.
@auth.route('/servers/delete/<int:server_id>')
@login_required
def delete(server_id):
    delete_server = Servers.query.get_or_404(server_id)

    try:
        db.session.delete(delete_server)
        db.session.commit()
        return redirect("/servers")

    except:
        return "There was a problem to delete the server"
