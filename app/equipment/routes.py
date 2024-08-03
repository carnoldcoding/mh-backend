from flask import Blueprint, request, jsonify
from app.equipment.service import get_weapons

# Register Blueprint (Allows for modular routing)
equipment = Blueprint("equipment", __name__)

@equipment.route("/get_weapons", methods=['GET'])
def weapons():
    weapon_type = request.args.get('type')
    
    return jsonify(get_weapons(weapon_type))