# import resprctive blueprints and flask REstful resources
from .blueprint_test import bp
from .user_routes import user
from .game_routes import game
from.transaction_routes import transaction
from .role_routes import role
from .bafflo_game_routes import bafflo

def add_resources(app):
    """
    Method to add resources to app context
    
    Args:
        app (object): object of Flask representing the app in context
    """
    pass

def register_blueprints(app):
    """
    Method to add blueprints to app context
    
    Args:
        app (object): object of Flask representing the app in context
    """
    app.register_blueprint(bp)
    app.register_blueprint(user)
    app.register_blueprint(game)
    app.register_blueprint(role)
    app.register_blueprint(transaction)
    app.register_blueprint(bafflo)