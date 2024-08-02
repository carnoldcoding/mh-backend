from flask import Blueprint
from app.equipment.service import get_weapons

# Register Blueprint (Allows for modular routing)
equipment = Blueprint("equipment", __name__)

@equipment.route("/")
def weapons():
    return get_weapons()