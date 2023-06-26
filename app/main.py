"""main.py - main code of A4A exercise"""
from fastapi import FastAPI
# project files
from players import Player


app = FastAPI()
player = Player(csv_file='../Data/Player.csv', debug=True)


@app.get("/api/players")
def get_players():
    return player.return_all()


@app.get("/api/players/{player_id}")
def get_player(player_id: str):
    return player.return_one(player_id=player_id)
