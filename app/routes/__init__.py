from app.routes.Loja import loja
from app.routes.auth import auth
from app.routes.admin import admin
from app import app

blueprints = [loja, auth, admin]

for blueprint in blueprints:
    app.register_blueprint(blueprint)

