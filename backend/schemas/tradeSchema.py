from pydantic import BaseModel
from .playerSchema import PlayerReturn


class TradeCreate(BaseModel):
    playerTrading:str
    playerWanted:str
    tradeTeam:str 

class TradeReturn(BaseModel):
    playerTraded:str
    playerRecieved:str
    tradeTeam:str
    yourTeam:str