from fastapi import FastAPI
from backend.db import Base, engine
from backend.models import Player, Team , GM
from backend.routes.players import router as players_router
from backend.routes.teams import router as team_router
from backend.routes.gm import router as gm_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(players_router)
app.include_router(team_router)
app.include_router(gm_router)
