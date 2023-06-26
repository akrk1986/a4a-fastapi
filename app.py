"""app.py - main code of A4A excercise"""
from fastapi import FastAPI
# project files
from players import Player


app = FastAPI()
player_obj = Player(csv_file='Data/Player.csv', debug=True)


@app.get("/api/players")
def get_players():
    return player_obj.return_all()


@app.get("/api/players/{player_id}")
def get_player(player_id: str):
    return player_obj.return_one(player_id=player_id)
