from pydantic import BaseModel
from backend.schemas.accountSchema import FantasyAccountReturn

class loginResponse(BaseModel):
    token: str
    account: FantasyAccountReturn