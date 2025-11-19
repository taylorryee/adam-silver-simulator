from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.schemas.teamSchema import TeamCreate, TeamReturn
from backend.schemas.tradeSchema import TradeReturn,TradeCreate
from backend.services import teamServices as service
#CRUD Create-post Read-get Update-put Delete-delete


router=APIRouter(prefix="/teams",tags=["TeamsRoutes"])

@router.post("/",response_model=TeamReturn)
def create_team_route(new_team:TeamCreate,db:Session=Depends(get_db)): #creates new team
    team = service.create_team(new_team,db)
    if not team:
        raise HTTPException(status_code=404, detail="That team already exists")
    return team

@router.get("/{team_name}",response_model=TeamReturn) 
def get_team(team_name:str,db:Session=Depends(get_db)): #gets a team
    team = service.get_team(team_name,db)
    if not team:
        raise HTTPException(status_code=404, detail="What team my boi that shit dont exist")
    return team

@router.put("/{team_name}/draft",response_model=TeamReturn)
def draft_player(team_name:str,player_name:str,db:Session=Depends(get_db)):
    team = service.draft_player(team_name,player_name,db)
    if not team:
        raise HTTPException(status_code=404, detail="What team my boi that shit dont exist")
    return team

@router.patch("/{team_name}/trade",response_model=TradeReturn)
def trade_player(team_name:str,trade:TradeCreate,db:Session=Depends(get_db)):
    trade = service.trade_player(team_name,trade,db)
    if not trade:
        raise HTTPException(status_code=404,detail="That trade ass")
    return trade


