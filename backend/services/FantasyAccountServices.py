from backend.security.auth import hash_password,verify_password,create_access_token
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


from backend.models import FantasyAccount
from backend.schemas.accountSchema import FantasyAccountCreate,FantasyAccountLogin,FantasyAccountReturn
from backend.schemas.loginSchema import loginResponse


def create_account(account:FantasyAccountCreate,db:Session):
    check_username= db.query(FantasyAccount).filter(FantasyAccount.username==account.username).first()
    if check_username:
        return None
    check_team_name= db.query(FantasyAccount).filter(FantasyAccount.team_name==account.team_name).first()
    if check_team_name:
        return None
    
    hashed_password = hash_password(account.password)
    newAccount = FantasyAccount(username = account.username, password = hashed_password,team_name=account.team_name)
    db.add(newAccount)
    try:
        db.commit()
        db.refresh(newAccount)
        return newAccount
    except IntegrityError:
        db.rollback()
        return None
    

def login(account:FantasyAccountLogin,db:Session):
    currentAccount= db.query(FantasyAccount).filter(FantasyAccount.username==account.username).first()
    if not currentAccount:
        return None
    verify = verify_password(account.password,currentAccount.password)
    if not verify:
        return None
    data = {"username":account.username}
    new_token = create_access_token(data)
    return loginResponse(token = new_token,account = currentAccount)


    



