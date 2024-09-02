from flask import Blueprint, render_template
import pathlib
import os

from app import src_admin

path = pathlib.Path(__file__).parent.resolve().__str__()
auth_template = os.path.join(path, "auth_template")

auth = Blueprint("auth", __name__, template_folder=auth_template, static_folder=src_admin)
@auth.route("/login")
def login():
    
    return render_template("login.html")