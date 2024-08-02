from flask import Blueprint

# Register Blueprint (Allows for modular routing)
equipment = Blueprint("equipment", __name__)

@equipment.route("/")
def weapons():
    return "Weapons"