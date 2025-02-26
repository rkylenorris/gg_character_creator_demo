from flask_sqlalchemy import SQLAlchemy
from character_sheet import CharacterClass, Race, Background
import json

# Initialize the database
db = SQLAlchemy()

class RaceModel(db.Model):
    
    __tablename__ = "Races"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    ability_score_increase = db.Column(db.JSON)
    size = db.Column(db.String(10), db.CheckConstraint("size IN ('Small', 'Medium', 'Large')"))
    speed = db.Column(db.Integer)
    traits = db.Column(db.JSON)
    languages = db.Column(db.JSON)


    def __init__(self, chosen_race: Race):
        super().__init__()
        self.name = chosen_race.name
        self.description = chosen_race.description
        self.ability_score_increase = json.dumps(chosen_race.ability_bonuses)
        self.size = chosen_race.size
        self.speed = chosen_race.speed
        self.traits = json.dumps(chosen_race.traits)
        self.languages = json.dumps(chosen_race.languages)
    
    def __repr__(self):
        return f"Race({self.name} - {self.description})"

