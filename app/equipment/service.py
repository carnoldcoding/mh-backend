from flask import jsonify
from app.equipment.model import Weapon

def get_weapons():
    weapons = Weapon.query.limit(5).all()
    weapon_list = [{'id': w.id } for w in weapons]
    return jsonify(weapon_list)