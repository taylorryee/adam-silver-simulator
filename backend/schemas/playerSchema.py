from pydantic import BaseModel
from typing import Optional

class PlayerCreate(BaseModel): #THis is for creating a player
    name: str
    age: int


class PlayerReturn(BaseModel):#THis is for returning a player, you need orm_mode on because you will be getting player 
    id: int                    #from db which will give u an orm object which needs to be converted back to be JSON
    name: str
    age: int
    team_id: Optional[int]
    class Config:
        from_attributes=True

class PlayerSimple(BaseModel):#This model is for using inside team. This Model specifically doesnt have a team_id 
    id:int                    #If it did have a team_id then it will keep a ciruclar loop inside team because player
    name:str                   # inside team would have the team attribute->which would cause infinte loop
    age:int                    #YOu also have orm_mode on here becaue you would be getting this value back from the db
    class Config:
        from_attributes=True


