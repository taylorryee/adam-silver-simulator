from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.schemas.accountSchema import FantasyAccountCreate ,FantasyAccountLogin ,FantasyAccountReturn
from backend.schemas.loginSchema import loginResponse
from backend.services import FantasyAccountServices as service
router = APIRouter(prefix="/account",tags=["fantasyAccount"])
    #ohh my - shit my boi im down bad rn idk. how ima make it oh shit but theyn u remeber
    #u been down bad oh u been down bad beofre but not just before u talking bout before before and before that 
    #u was down bad before dat and not just before after u been down bad after and now we talkin future tense oh lawd
    #shit just been bad in this lifetime aint it dam that shit crazy - u gon be good tho cuz at least u know were u at in
    #life cuz u been there beforreeee yeaaa oh lawwdd
#CRUD Create-post Read-get Update-put/patch Delete-delte
@router.post("/create",response_model=FantasyAccountReturn)
def create_account_route(account:FantasyAccountCreate,db:Session=Depends(get_db)):
    new_account = service.create_account(account,db)
    return new_account


@router.post("/login",response_model=loginResponse)
def login_to_account_route(account:FantasyAccountLogin,db:Session=Depends(get_db)):
    login_to_acc = service.login(account,db)
    return login_to_acc
