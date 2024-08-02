from app import db

class Weapon(db.Model):
    __tablename__ = "weapon"

    id = db.Column(db.Integer, primary_key=True)
    create_recipe_id = db.Column(db.Integer)
    upgrade_recipe_id = db.Column(db.Integer)
    previous_weapon_id = db.Column(db.Integer)
    armorset_bonus_id = db.Column(db.Integer)

    rarity = db.Column(db.Integer)
    category = db.Column(db.Text)
    attack = db.Column(db.Integer)
    attack_true = db.Column(db.Integer)
    affinity = db.Column(db.Integer)
    defense = db.Column(db.Integer)

    slot_1 = db.Column(db.Integer)
    slot_2 = db.Column(db.Integer)
    slot_3 = db.Column(db.Integer)

    phial = db.Column(db.Text)
    phial_power = db.Column(db.Integer)
    shelling = db.Column(db.Text)
    shelling_level = db.Column(db.Integer)