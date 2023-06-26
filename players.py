"""Handle the players data."""

import csv
from pathlib import Path
from fastapi import HTTPException


class Player:
    def __init__(self, csv_file: str, debug: bool):
        self.csv_file = csv_file
        self.debug = debug

        csv_path = Path(self.csv_file)
        if not csv_path.is_file():
            return
            raise HTTPException(status_code=500,
                                detail=f"Error: Players file '{self.csv_file}' is not accessible or is not a file",
                                headers={"X-Error": "Players CSV file is not found at expected location"})
