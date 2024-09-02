from flask import Blueprint, render_template
import os
import pathlib

from app import src_store

path = pathlib.Path(__file__).parent.resolve().__str__()
loja_template = os.path.join(path, "loja_template")

loja = Blueprint("loja", __name__, template_folder="loja_template", static_folder=src_store)
@loja.route("/store")
def store():
    
    return render_template("store.html")