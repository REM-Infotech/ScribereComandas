from flask import Flask, render_template, url_for, redirect, make_response
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from configs import csp
from datetime import timedelta
import pathlib
import os

src_store = os.path.join(pathlib.Path(__file__).parent.resolve().__str__(), "src_store")
src_admin = os.path.join(pathlib.Path(__file__).parent.resolve().__str__(), "src_admin")

files_render = os.path.join(os.getcwd(), "src")
app = Flask(__name__, template_folder = files_render, static_folder = files_render)

app.config.from_object("app.default_config")

# db = SQLAlchemy()
# tlsm = Talisman()
# login_manager = LoginManager()

# db.init_app(app)
# login_manager.init_app(app)

# age = timedelta(days=7).max.seconds
# tlsm.init_app(app, content_security_policy=csp(),
#               session_cookie_http_only=True,
#               session_cookie_samesite='Lax',
#               strict_transport_security=True,
#               strict_transport_security_max_age=age,
#               x_content_type_options= True,
#               x_xss_protection=True)

from app import routes

@app.route("/", methods = ["GET"])
def index():
    
    response = make_response(redirect(url_for("loja.store")))
    return response, 302