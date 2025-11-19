from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from backend.models import Team, Player
from backend.schemas.playerSchema import PlayerCreate


def create_player(db:Session,newPlayer:PlayerCreate):
    newPlayer = Player(name = newPlayer.name,age = newPlayer.age)
    db.add(newPlayer)

    try:
        db.commit()
        db.refresh(newPlayer)
        return newPlayer
    except IntegrityError:
        db.rollback()
        return None


def get_player(db:Session,player_id:int):
    return db.query(Player).filter(Player.id==player_id).first()

def get_all_players(db:Session):
    return db.query(Player).all()

def get_all_available_players(db:Session):
    return db.query(Player).filter(Player.team_id==None).all()
    
