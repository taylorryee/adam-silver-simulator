from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.schemas.gmSchema import GmCreate, GmReturn
from backend.services import GmServices as service

#CRUD Create-post Read-get Update-put Delete-delete

router = APIRouter(prefix ="/gm",tags=["LeGM"])

@router.post("/",response_model=GmReturn)
def create_gm(newGM:GmCreate,db:Session=Depends(get_db)):
    gm = service.create_gm(newGM,db)
    if not gm:
        raise HTTPException(status_code=404, detail="That team already gotta gm")
    return gm

@router.get("/{team_name}",response_model=GmReturn)
def get_gm(team_name:str,db:Session=Depends(get_db)):
    gm = service.get_gm(team_name,db)
    if not gm:
        raise HTTPException(status_code=404, detail="Them boiz got no gm")
    return gm 

@router.delete("/{team_name}")
def fire_gm(team_name:str,db:Session=Depends(get_db)):
    fired = service.fire_gm(team_name,db)
    if not fired:
        raise HTTPException(status_code=404, detail="bru who u firing they got no gm")
    return{"fired gm": fired.name}