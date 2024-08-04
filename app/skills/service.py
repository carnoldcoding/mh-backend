from app.skills.model import Skill, SkillTree, SkillTreeText
from app import db
from sqlalchemy import select

def get_skills():

    stmt = select(Skill).join(SkillTree).where(Skill.lang_id == "en")
    
    result = db.session.scalars(stmt.limit(50))

    skill_data = [{
        "level" : sd.level,
        "description" : sd.description,
        "skill_tree": {
            "max_level": sd.skill_tree.max_level,
            "icon_color" : sd.skill_tree.icon_color,
            "secret" : sd.skill_tree.secret,
            "unlocks_id" : sd.skill_tree.unlocks_id
        }
    } for sd in result]


    return skill_data