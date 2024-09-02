from flask import Blueprint, render_template
import pathlib
import os

from app import src_admin

path = pathlib.Path(__file__).parent.resolve().__str__()
admin_template = os.path.join(path, "admin_template")

admin = Blueprint("admin", __name__, template_folder=admin_template, static_folder=src_admin)
@admin.route("/dashboard")
def dashboard():
    
    return render_template("dashboard.html")