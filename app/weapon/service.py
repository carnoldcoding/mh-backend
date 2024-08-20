from app import db
from sqlalchemy import select, Table, MetaData, and_

metadata = MetaData()

def get_weapon_data(weapon_name : str):
    #Define Tables
    weapon = Table('weapon', metadata, autoload_with=db.engine)
    weapon_skill = Table('weapon_skill', metadata, autoload_with=db.engine)
    weapon_text = Table('weapon_text', metadata, autoload_with=db.engine)

    #Define Statement
    stmt = select(weapon, weapon_text, weapon_skill)\
        .select_from(weapon.join(weapon_text, weapon.c.id == weapon_text.c.id)\
            .join(weapon_skill, weapon.c.id == weapon_skill.c.weapon_id, isouter=True))\
        .where(and_(weapon_text.c.lang_id == 'en', weapon_text.c.name.ilike(f'%{weapon_name}%')))\
        .limit(10)

    #Execute, Parse and Return
    result = db.session.execute(stmt)
    map = [dict(row._mapping) for row in result]
    return map