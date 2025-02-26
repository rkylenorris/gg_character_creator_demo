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


class BackgroundModel(db.Model):
    
    __tablename__ = "Backgrounds"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    feature = db.Column(db.JSON)
    skill_proficiencies = db.Column(db.JSON)
    tool_proficiencies = db.Column(db.JSON)
    starting_equipment = db.Column(db.JSON)


    def __init__(self, chosen_background: Background):
        super().__init__()
        self.name = chosen_background.name
        self.description = chosen_background.description
        self.feature = json.dumps(chosen_background.feature)
        self.skill_proficiencies = json.dumps(chosen_background.skill_proficiencies)
        self.tool_proficiencies = json.dumps(chosen_background.tool_proficiencies)
        self.starting_equipment = json.dumps(chosen_background.equipment)
        
    def __repr__(self):
        return f"Background({self.name} - {self.description})"


class ClassModel(db.Model):
    __tablename__ = "Classes"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    hit_die = db.Column(db.Text)
    primary_abilities = db.Column(db.JSON)
    saving_throws = db.Column(db.JSON)
    proficiencies = db.Column(db.JSON)
    skills = db.Column(db.JSON)
    starting_equipment = db.Column(db.JSON)
    starting_ability_scores = db.Column(db.JSON)
    description = db.Column(db.Text)
    role = db.Column(db.Text)
    
    def __init__(self, chosen_class: CharacterClass):
        super().__init__()
        self.name = chosen_class.name
        self.hit_die = chosen_class.hit_die
        self.primary_abilities = json.dumps(chosen_class.primary_abilities)
        self.saving_throws = json.dumps(chosen_class.saving_throws)
        self.proficiencies = json.dumps(chosen_class.proficiencies)
        self.skills = json.dumps(chosen_class.skills)
        self.starting_equipment = json.dumps(chosen_class.starting_equipment)
        self.starting_ability_scores = json.dumps(chosen_class.starting_ability_scores)
        self.description = chosen_class.description
        self.role = chosen_class.role
    
    def __repr__(self):
        return f"Class({self.name} - {self.hit_die})"