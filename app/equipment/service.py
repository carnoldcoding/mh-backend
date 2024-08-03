from app.equipment.model import Weapon, WeaponSkill, WeaponText
from app import db
from sqlalchemy import select

def get_weapons(weapon_type):
    stmt = select(Weapon, WeaponText).join(WeaponText.weapon).where(WeaponText.lang_id == "en")
    
    if weapon_type:
        stmt = stmt.where(Weapon.weapon_type == weapon_type)
    
    weapon_data = db.session.scalars(stmt.limit(10))

    weapon_list = [{
        'id': w.id ,
        'create_recipe_id': w.create_recipe_id,
        'upgrade_recipe_id': w.upgrade_recipe_id,
        'previous_weapon_id': w.previous_weapon_id,
        'armorset_bonus_id' : w.armorset_bonus_id,

        'weapon_type' : w.weapon_type,

        'rarity': w.rarity,
        'category': w.category,
        'attack': w.attack,
        'attack_true': w.attack_true,
        'affinity' : w.affinity,
        'defense' : w.defense,
        'sharpness': w.sharpness,
        'sharpness_maxed': w.sharpness_maxed,

        'element1' : w.element1,
        'element1_attack' : w.element1_attack,
        'element2' : w.element2,
        'element2_attack' : w.element2_attack,
        'element_hidden' : w.element_hidden,

        'elderseal' : w.elderseal,
        
        'slot_1' : w.slot_1,
        'slot_2' : w.slot_2,
        'slot_3' : w.slot_3,

        'phial' : w.phial,
        'phial_power' : w.phial_power,
        'shelling' : w.shelling,
        'shelling_level' : w.shelling_level,

        'kinsect_bonus' : w.kinsect_bonus,

        'coating_close' : w.coating_close,
        'coating_power' : w.coating_power,
        'coating_paralysis': w.coating_paralysis,
        'coating_poison' : w.coating_poison,
        'coating_sleep' : w.coating_sleep,
        'coating-blast' : w.coating_blast,
        'ammo_id' : w.ammo_id,
        'weapon_text': [{
            'name': wt.name
        }for wt in w.weapon_text]

    } for w in weapon_data]

    return weapon_list
