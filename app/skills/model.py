from app import db

class Skill(db.Model):
    __tablename__ = "skill"

    skilltree_id = db.Column(db.Integer, db.ForeignKey('skilltree.id'), primary_key = True)
    lang_id = db.Column(db.Text)
    level = db.Column(db.Integer)
    description = db.Column(db.Text)

    skill_tree = db.relationship('SkillTree')
    skilltree_text = db.relationship('SkillTree')

class SkillTree(db.Model):
    __tablename__ = "skilltree"

    id = db.Column(db.Integer, primary_key = True)
    max_level = db.Column(db.Integer)
    icon_color = db.Column(db.Text)
    secret = db.Column(db.Integer)
    unlocks_id = db.Column(db.Integer)

class SkillTreeText(db.Model):
    __tablename__ = "skilltree_text"

    id = db.Column(db.Integer, primary_key = True)
    lang_id = db.Column(db.Text)
    name = db.Column(db.Text)
    description = db.Column(db.Text)