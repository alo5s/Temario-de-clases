from flask import Blueprint, render_template, request
from routes.auth import user_login_required


view_home = Blueprint('home',__name__)

@view_home.route("/")
@user_login_required
def home():
    return render_template("home.html")
