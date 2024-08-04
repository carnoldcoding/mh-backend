from app import db
from sqlalchemy import select, Table, MetaData, and_

metadata = MetaData()

def get_skill_data():
    #Define Tables
    skilltree = Table('skilltree', metadata, autoload_with=db.engine)
    skilltree_text = Table('skilltree_text', metadata, autoload_with=db.engine)
    skill = Table('skill', metadata, autoload_with=db.engine)

    #Define Statement
    stmt = select(skill, skilltree, skilltree_text)\
        .select_from(skill.join(skilltree, skill.c.skilltree_id == skilltree.c.id)
                     .join(skilltree_text, skilltree.c.id == skilltree_text.c.id))\
        .where(and_(skill.c.lang_id == "en", skilltree_text.c.lang_id == "en"))\
        .limit(10)
    
    #Execute, Parse and Return
    result = db.session.execute(stmt)
    map = [dict(row._mapping) for row in result]
    return map