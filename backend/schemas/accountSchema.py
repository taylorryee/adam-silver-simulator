from pydantic import BaseModel
from playerSchema import PlayerSimple
from typing import List

class FantasyAccountCreate(BaseModel):
    username:str
    password:str
    team_name: str

class FantasyAccountLogin(BaseModel):
    username:str
    password:str

class FantasyAccountReturn(BaseModel):
    id:int
    team_name:str
    username:str
    roster:List[PlayerSimple]=[]
    class Config:
        from_attributes=True

