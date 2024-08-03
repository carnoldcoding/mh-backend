from app import db

class WeaponText(db.Model):
    __tablename__ = "weapon_text"

    id = db.Column(db.Integer, db.ForeignKey('weapon.id'), primary_key = True)
    lang_id = db.Column(db.Text)
    name = db.Column(db.Text)
    weapon = db.relationship('Weapon', backref=db.backref('weapon_text', lazy=True))
    #db.relationship ties WeaponText back to Weapon, under the property 'weapon_text'
    #this states that every WeaponText has a Weapon, and Weapons can have many WeaponText

class WeaponSkill(db.Model):
    __tablename__ = "weapon_skill"

    weapon_id = db.Column(db.Integer, db.ForeignKey('weapon.id'), primary_key = True)
    skilltree_id = db.Column(db.Integer)
    level = db.Column(db.Integer)


class Weapon(db.Model):
    __tablename__ = "weapon"

    id = db.Column(db.Integer, primary_key=True)
    create_recipe_id = db.Column(db.Integer)
    upgrade_recipe_id = db.Column(db.Integer)
    previous_weapon_id = db.Column(db.Integer)
    armorset_bonus_id = db.Column(db.Integer)

    weapon_type = db.Column(db.Text)

    rarity = db.Column(db.Integer)
    category = db.Column(db.Text)
    attack = db.Column(db.Integer)
    attack_true = db.Column(db.Integer)
    affinity = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    sharpness = db.Column(db.Integer)
    sharpness_maxed = db.Column(db.Boolean)

    element1 = db.Column(db.Text)
    element1_attack = db.Column(db.Integer)
    element2 = db.Column(db.Text)
    element2_attack = db.Column(db.Integer)
    element_hidden = db.Column(db.Boolean)

    elderseal = db.Column(db.Text)

    slot_1 = db.Column(db.Integer)
    slot_2 = db.Column(db.Integer)
    slot_3 = db.Column(db.Integer)

    phial = db.Column(db.Text)
    phial_power = db.Column(db.Integer)
    shelling = db.Column(db.Text)
    shelling_level = db.Column(db.Integer)

    kinsect_bonus = db.Column(db.Text)

    coating_close = db.Column(db.Integer)
    coating_power = db.Column(db.Integer)
    coating_paralysis = db.Column(db.Integer)
    coating_poison = db.Column(db.Integer)
    coating_sleep = db.Column(db.Integer)
    coating_blast = db.Column(db.Integer)
    ammo_id = db.Column(db.Integer)
