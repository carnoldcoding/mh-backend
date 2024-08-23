from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.extensions import db
import os

#Import Blueprints
from app.weapon.routes import weapon

def create_app():
    #Load Environemntal Variables
    load_dotenv()

    # Initialize Flask Instance
    app = Flask(__name__)
    CORS(app)

    #Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(weapon)
    return app