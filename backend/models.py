from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base
#Think of your database like tables in SQL, and SQLAlchemy like a translator that turns rows into Python objects.

class Team(Base): #This is basically a Python class that maps to the teams table in your database.
    #Each instance of Team represents one row in that table.
    __tablename__="teams"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,index=True)
    players = relationship("Player",back_populates="team")
    gm = relationship("GM",back_populates="team",uselist=False) #useList tells team that there is only 1 GM so you should only 
    #return 1 object,not a list

class Player(Base):#This is basically a Python class that maps to the Players table in your database.
#Each instance of Player represents one row in that table.
    __tablename__="players"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,index=True)
    age = Column(Integer,index=True)
    
    team_id=Column(Integer,ForeignKey("teams.id"),nullable=True) #This line is what actually connects the SQL tables. 
 # This line is what actually connects the SQL tables.
    # "teams.id" is saying:
        #   → go to the "teams" table
        #   → and reference the "id" column.The foreign key line always goes
    #in the child table - meaning the table that points to another table - in this case  a player points to its team. 
    
    team=relationship("Team",back_populates="players")#This line on the other hand is purely for python convenience. 
    #This lets you do things like player.team. # SQLAlchemy uses the ForeignKey above (team_id → teams.id)
# to automatically fetch the correct Team object when you access player.team.
    

class GM(Base):
    __tablename__ = "gm"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,index=True)
    team = relationship("Team",back_populates = "gm")
    team_id = Column(Integer, ForeignKey("teams.id"), unique=True)