from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from collections import defaultdict

app = FastAPI()

class Team(BaseModel):
    name: str
    zone: str
    difference: int
    points: int

app = FastAPI()

@app.post("/positions/", response_model=List[Team])
def getPositions(teams: List[Team]):
    # Sort all the teams, points and the difference with second priority
    sorted_teams = sorted(teams, key=lambda x: (x.points, x.difference), reverse=True)
    return sorted_teams

@app.post("/positions_by_zone/")
def getPositionsByZone(teams: List[Team]):
    # Group by zone
    zones: Dict[str, List[Team]] = defaultdict(list)

    for team in teams:
        zones[team.zone].append(team)

    # Sort the teams by zone
    for zone in zones:
        zones[zone] = sorted(zones[zone], key=lambda x: (x.points, x.difference), reverse=True)

    return zones