#create get delete

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from backend.models import Team, Player,GM
from backend.schemas.gmSchema import GmCreate


def create_gm(newGM:GmCreate,db:Session):
    team = db.query(Team).filter(Team.name==newGM.team).first()
    if not team:
        return None
    leGm=GM(name=newGM.name,team_id=team.id)
    #leGm.id = team.id
    db.add(leGm)
    try:
        db.commit()
        db.refresh(leGm)
        return leGm
    except IntegrityError:
        db.rollback()
        return None

def get_gm(team_name:str,db:Session):
    team = db.query(Team).filter(Team.name==team_name).first()
    if not team:
        return None
    
    return db.query(GM).filter(GM.team_id==team.id).first()

def fire_gm(team_name:str,db:Session):
    team = db.query(Team).filter(Team.name==team_name).first()
    if not team:
        return None
    
    gm = db.query(GM).filter(GM.team_id==team.id).first()
    if not gm:
        return None
    db.delete(gm)
    db.commit()
    return gm

