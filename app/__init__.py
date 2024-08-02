from flask import Flask
from flask_cors import CORS
from app.equipment.routes import equipment

def create_app():

    # Initialize Flask Instance
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(equipment)
    
    return app