from pydantic import BaseModel
from .playerSchema import PlayerSimple
from .gmSchema import GmSimple
from typing import List,Optional

class TeamCreate(BaseModel): #Creates team
    name:str

class TeamReturn(BaseModel): #Returns team, you need to use PlayerSimple to ensure that there is no ciruclar dependancy
    id:int                   #Also you need to have orm_mode on because you will be getting team from db which will be ORM object
    name:str
    players:List[PlayerSimple]=[]
    gm: Optional[GmSimple]
    class Config:
        from_attributes=True

