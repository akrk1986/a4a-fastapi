# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
# project files
from players import Player


app = FastAPI()

players_loaded = False


def _find_next_id():
    return max(country.country_id for country in countries) + 1


class Country(BaseModel):
    country_id: int = Field(default_factory=_find_next_id, alias="id")
    name: str
    capital: str
    area: int


countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513120),
    Country(id=2, name="Australia", capital="Canberra", area=7617930),
    Country(id=3, name="Egypt", capital="Cairo", area=1010408),
]

countries_dict = {}
for country in countries:
    countries_dict[country.country_id] = country.name


@app.get("/api/players")
async def get_players():
    fu = Player(csv_file='players.csv', debug=True)
    return countries


@app.get("/api/players/{player_id}")
async def get_player(player_id: int):
    if not players_loaded:
        fu = Player(csv_file='players.csv', debug=True)
    if player_id in countries_dict:
        return countries_dict[player_id]
    raise HTTPException(status_code=404,
                        detail=f"Error: no player with ID '{player_id}'")

