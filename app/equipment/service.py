from flask import jsonify
from app.equipment.model import Weapon

def get_weapons():
    weapons = Weapon.query.limit(10).all()
    weapon_list = [{
        'id': w.id ,
        'create_recipe_id': w.create_recipe_id,
        'upgrade_recipe_id': w.upgrade_recipe_id,
        'previous_weapon_id': w.previous_weapon_id,
        'armorset_bonus_id' : w.armorset_bonus_id,

        'rarity': w.rarity,
        'category': w.category,
        'attack': w.attack,
        'attack_true': w.attack_true,
        'affinity' : w.affinity,
        'defense' : w.defense,
        
        'slot_1' : w.slot_1,
        'slot_2' : w.slot_2,
        'slot_3' : w.slot_3,

        'phial' : w.phial,
        'phial_power' : w.phial_power,
        'shelling' : w.shelling,
        'shelling_level' : w.shelling_level

        } for w in weapons]
    return jsonify(weapon_list)