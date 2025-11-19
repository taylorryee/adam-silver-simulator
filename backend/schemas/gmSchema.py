from pydantic import BaseModel
from typing import Optional

class GmCreate(BaseModel): #creating a GM
    name : str
    team : str

class GmSimple(BaseModel):
    name : str
    class Config:
        from_attributes = True

class GmReturn(BaseModel): #returning gm form db 
    name : str
    team_id  :int
    class Config:
        from_attributes = True