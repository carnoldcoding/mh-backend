from flask import Blueprint, jsonify, request
from app.weapon.service import get_weapon_data

weapon = Blueprint('weapon', __name__)

@weapon.route('/get_weapon')
def get_weapon():
    weapon_name = request.args.get('name')
    return jsonify(get_weapon_data(weapon_name))