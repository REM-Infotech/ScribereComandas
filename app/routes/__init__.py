from app.routes.Loja import loja
from app.routes.auth import auth
from app import app

blueprints = [loja, auth]

for blueprint in blueprints:
    app.register_blueprint(blueprint)

