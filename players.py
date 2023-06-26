"""Handle the Player.csv data."""

import csv
from pathlib import Path
from fastapi import HTTPException


class Player:
    def __init__(self, csv_file: str, debug: bool):
        self.csv_file = csv_file
        self.debug = debug
        self.rows = []          # list of dicts
        self.rows_dict = {}
        print(f"CSV='{csv_file}'")
        csv_path = Path(self.csv_file)
        if not csv_path.is_file():
            raise HTTPException(
                status_code=500,
                detail=f"Error: Players file '{self.csv_file}' is not accessible or is not a file")

        with csv_path.open(mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.rows.append(row)
                player_id = row['playerID']
                if player_id in self.rows_dict:
                    raise HTTPException(
                        status_code=500,
                        detail=f"Error: Players file '{self.csv_file}' has a duplicate Player ID '{player_id}'")
                self.rows_dict[player_id] = row

    def return_all(self):
        return self.rows

    def return_one(self, player_id: str):
        if player_id in self.rows_dict:
            return self.rows_dict[player_id]
        raise HTTPException(status_code=404,
                            detail=f"Error: Player ID '{player_id}' is not a valid Player ID")
