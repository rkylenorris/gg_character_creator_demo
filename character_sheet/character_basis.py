import json
from pathlib import Path

class CharacterClass:
    def __init__(self, name: str, hit_die: str, primary_abilities: list[str], saving_throws: list[str],
                 proficiencies : dict[str, list[str]], skills: list[str],
                 starting_equipment: list[str], starting_ability_scores: dict[str, int],
                 desc: str, role: str):
        self.name = name
        self.hit_die = hit_die
        self.primary_abilities = primary_abilities
        self.saving_throws = saving_throws
        self.proficiencies  = proficiencies 
        self.skills = skills
        self.starting_equipment = starting_equipment
        self.starting_ability_scores = starting_ability_scores
        self.description = desc
        self.role = role
        
    @classmethod
    def load_class(cls, class_name: str):
        # Load class data from a file or database
        classes_path = Path('data/classes.json')
        with open(classes_path, 'r') as f:
            classes = json.load(f)
        class_data = next(iter([c for c in classes if c['name'] == class_name]), None)
        if class_data:
            return cls(**class_data)
        else:
            raise ValueError(f"Class '{class_name}' not found")


class Race:
    def __init__(self, name: str, description: str,
                 ability_score_increase: dict[str, int], size: int,
                 speed: int, traits: list[str], languages: list[str]):
        self.name = name
        self.description = description
        self.ability_bonuses = ability_score_increase
        self.size = size
        self.speed = speed
        self.traits = traits
        self.languages = languages
    
    @classmethod
    def load_race(cls, race_name: str):
        # Load race data from a file or database
        races_path = Path('data/races.json')
        with open(races_path, 'r') as f:
            races = json.load(f)
        race = next(iter([race for race in races if race['name'] == race_name]), None)
        if race:
            return cls(**race)
        else:
            raise ValueError(f"Race '{race_name}' not found")
        
        
class Background:
    def __init__(self, name: str, description: str, feature: dict[str, str],
                 skill_proficiencies: list[str], tool_proficiencies: list[str],
                 starting_equipment: list[str]):
        self.name = name
        self.description = description
        self.skill_proficiencies = skill_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.equipment = starting_equipment
        self.feature = feature
    
    @classmethod
    def load_background(cls, background_name: str):
        # Load background data from a file or database
        backgrounds_path = Path('data/backgrounds.json')
        with open(backgrounds_path, 'r') as f:
            backgrounds = json.load(f)
        background = next(iter([bg for bg in backgrounds if bg['name'] == background_name]), None)
        if background:
            return cls(**background)
        else:
            raise ValueError(f"Background '{background_name}' not found")