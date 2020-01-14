from .main import admin

def register_adminBluePrint(app):
    app.register_blueprint(admin)
