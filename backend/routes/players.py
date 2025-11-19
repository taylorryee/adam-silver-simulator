from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.schemas.playerSchema import PlayerCreate, PlayerReturn
from backend.services import playerServices as service
#CRUD Create-post Read-get Update-put Delete-delete

router = APIRouter(prefix="/players", tags=["PlayersRoutes"]) #Creates router,his is saying that all routes under 
#this will be under /players, Tags is for swagger ui to group all these routers under "Players"

@router.post("/", response_model=PlayerReturn)
def create_player_route(new_player: PlayerCreate, db: Session = Depends(get_db)): #Creates DB session and passes to route
    player = service.create_player(db,new_player)
    return player

@router.get("/available",response_model=list[PlayerReturn]) #REMEBER ALL STATIC ROUTES MUST COME BEFORE DYNAMIC ROUTES. 
#MOST WEB FRAMEWORKS MATCH TOP-BOTTOM SO IF IT SEES A DYNAMIC ROUTE THEN IT WILL AUTOAMTICALLY TRY TO MATCH say "availble"
#TO {player_id}
def get_all_available_players(db:Session=Depends(get_db)):
    players = service.get_all_available_players(db)
    return players

@router.get("/", response_model=list[PlayerReturn])
def get_all_players_route(db: Session = Depends(get_db)):
    players = service.get_all_players(db)
    return players

@router.get("/{player_id}", response_model=PlayerReturn) #THIS IS A DYNAMIC ROUTE AND IT MUST COME AFTER ALL THE STATIC ROUTES ABOVE
def get_player_route(player_id: int, db: Session = Depends(get_db)):
    player = service.get_player(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="That boi dont exist")
    return player



