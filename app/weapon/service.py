from app import db
from sqlalchemy import select, Table, MetaData, and_
from app.skills.service import get_skill_data

metadata = MetaData()

def get_weapon_data(weapon_name : str):
    #Define Tables
    weapon = Table('weapon', metadata, autoload_with=db.engine)
    weapon_skill = Table('weapon_skill', metadata, autoload_with=db.engine)
    weapon_text = Table('weapon_text', metadata, autoload_with=db.engine)
    weapon_ammo = Table('weapon_ammo', metadata, autoload_with=db.engine)
    weapon_melody = Table('weapon_melody', metadata, autoload_with=db.engine)
    weapon_melody_notes = Table('weapon_melody_notes', metadata, autoload_with=db.engine)
    weapon_melody_text = Table('weapon_melody_text', metadata, autoload_with=db.engine)
    
    # Get subquery
    skill_data = get_skill_data()

    #Define Statement
    stmt = select(weapon,
                   weapon_text, 
                   weapon_text.c.name.label('weapon_name'),
                   weapon_skill, 
                  skill_data.c.description.label('skill_description'),
                  skill_data.c.level.label('skill_level'),
                  skill_data.c.name.label('skill_name'))\
        .select_from(weapon.join(weapon_text, weapon.c.id == weapon_text.c.id)\
            .join(weapon_skill, weapon.c.id == weapon_skill.c.weapon_id, isouter=True))\
            .join(skill_data, weapon_skill.c.skilltree_id == skill_data.c.id, isouter=True)\
        .where(and_(weapon_text.c.lang_id == 'en', 
                    weapon_text.c.name.ilike(f'{weapon_name}%')))\
        .limit(10)

    #Execute, Parse and Return
    result = db.session.execute(stmt)
    map = [dict(row._mapping) for row in result]
    return map