from interfaces import IStatSaver
from typing import Dict
import json
import os


class StatSaver(IStatSaver):
    def __init__(self, filename: str = "stat.json"):
        self.filename = filename
    
    def save_state(self, balance: float, ingredients: Dict[str, int], day: int) -> None:
        state = {
            "balance": balance,
            "ingredients": ingredients,
            "day": day
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    
    def load_state(self) -> Dict:
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            return {
                "balance": 1000.0,
                "ingredients": {},
                "day": 1
            }
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {
                "balance": 1000.0,
                "ingredients": {},
                "day": 1
            }
