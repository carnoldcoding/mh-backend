from app import db
from sqlalchemy import select, Table, MetaData, and_, bindparam

metadata = MetaData()

def get_skill_data():
    #Define Tables
    skilltree = Table('skilltree', metadata, autoload_with=db.engine)
    skilltree_text = Table('skilltree_text', metadata, autoload_with=db.engine)
    skill = Table('skill', metadata, autoload_with=db.engine)

    #Define Subquery
    stmt = select(skill.c.description,
                  skill.c.level,
                   skilltree, 
                   skilltree_text.c.name)\
        .select_from(skill.join(skilltree, skill.c.skilltree_id == skilltree.c.id)
                     .join(skilltree_text, skilltree.c.id == skilltree_text.c.id))\
        .where(and_(skill.c.lang_id == "en", 
                    skilltree_text.c.lang_id == "en")).subquery()
    return stmt