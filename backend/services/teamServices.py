from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from backend.models import Team, Player
from backend.schemas.teamSchema import TeamCreate
from backend.schemas.tradeSchema import TradeCreate,TradeReturn
import string

def create_team(team_payload: TeamCreate, db: Session) -> Team | None:#When you get a post call 
    #fastAPI converts it to a TeamCreate object which you pass into this function.

    new_team = Team(name=team_payload.name) #This creates a new ORM Team Object which is the Python class that maps to the Team table 
    #in the SQLALchemy DB that you defined in Models.py. Then you set the name field in your Team model to the 
    #name field inside your Pydantic model TeamCreate.
    
    db.add(new_team)#At this point new_team is just a python object, here you are telling the db you want to add it
    try:
        db.commit()#This command actually adds new_team to the db
        db.refresh(new_team)  # This ensures that any values the database generated 
        #are loaded back into the Python object. Here id is the primary_key so the db automacitly increments and generates it
        return new_team
    except IntegrityError:#This raises SQLALchemy error if there are constraint violations of the Team model.
        #In this function it checks for another team with same name because in your SQL ORM Team model you set name to unique.
        db.rollback()#Rolls back the actions done in this session
        return None




def get_team(team_name:string,db:Session):
    return db.query(Team).filter(Team.name==team_name).first()
# Starts a query on the Team table.
# Filter restricts the query to only rows where id == team_id.
# .first() executes the query and returns the first row found (or None if no match).
# The returned object is a SQLAlchemy ORM object.
# When this function is called in teams.py and returned from the route,
# FastAPI uses the response_model (TeamReturn) to convert the ORM object to JSON.
# TeamReturn is defined in teamSchema.py, and orm_mode = True tells Pydantic
# how to serialize ORM objects into JSON.

#FINISH DRAFT PLAYR< GO TO GYM NOW TWIN YOU DESRVER THIS GOOD LEARNING TODAY


def draft_player(team_name: str, player_name: str, db: Session) -> Team | None:

    team = db.query(Team).filter(Team.name == team_name).first()
    player = db.query(Player).filter(Player.name == player_name).first()
 
    if not team or not player or player.team is not None:
        return None

    # Assign the player to the team
    player.team_id = team.id
    db.add(player)
    db.commit()
    db.refresh(team)  # refresh team so players relationship updates
    return team


def trade_player(team_name:str,trade:TradeCreate,db:Session):
    #verify that player wanted exists and get player wanted object
    playerWanted = db.query(Player).filter(Player.name==trade.playerWanted).first()
    if not playerWanted:
        return None
    #verify that team you want to trade with exists and get team object
    trade_team = db.query(Team).filter(Team.name==trade.tradeTeam).first()
    if not trade_team:
        return None
    #verify that the player you want is on the team you are trading with
    if playerWanted.team_id!=trade_team.id:
        return None
    #get player object that you are trading
    playerTrading=db.query(Player).filter(Player.name==trade.playerTrading).first()
    if not playerTrading:
        return None
    
    #get your team object
    yourTeam = db.query(Team).filter(Team.name==team_name).first()
    if not yourTeam:
        return None
    #verify that player you are trading is on your team
    if playerTrading.team_id!=yourTeam.id:
        return None
    #intiate the trade
    playerTrading.team_id,playerWanted.team_id = playerWanted.team_id,playerTrading.team_id
    
    db.add(playerTrading)
    db.add(playerWanted)
    succesfulTrade = TradeReturn(playerTraded=
                                 playerTrading.name,playerRecieved=
                                 playerWanted.name,tradeTeam=
                                 trade_team.name,yourTeam=
                                 yourTeam.name)
    try:
        db.commit()
        db.refresh(playerTrading)
        db.refresh(playerWanted)
        return succesfulTrade
    except IntegrityError:
        db.rollback()
        return None








