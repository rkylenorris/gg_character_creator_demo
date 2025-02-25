from dataclasses import dataclass
from typing import Union
from random import randint
from pathlib import Path
import json


@dataclass
class HitPoints:
    max_hp: int = 0
    current_hp: int = 0
    temp_hp: int = 0
    
    def roll_hit_points(self, hit_die: str, ability_modifier: int, level: int = 1):
        hit_die_size = int(hit_die[1:])  # Extracts the number from 'd8', 'd10', etc.
        if level > 1:
            hit_die_size = randint(1, hit_die_size)
        self.max_hp += hit_die_size + ability_modifier
        self.current_hp = self.max_hp


class AbilityScores:
    might: int
    reflexes: int
    endurance_core: int
    arcane_logic: int
    aether_sense: int
    presence: int
    
    def __init__(self, starting_scores: dict[str, int]):
        self.might = starting_scores.get('might', 0)
        self.reflexes = starting_scores.get('reflexes', 0)
        self.endurance_core = starting_scores.get('endurance_core', 0)
        self.arcane_logic = starting_scores.get('arcane_logic', 0)
        self.aether_sense = starting_scores.get('aether_sense', 0)
        self.presence = starting_scores.get('presence', 0)
        
    def increase_ability_score(self, ability: str, amount: int):
        if hasattr(self, ability):
            setattr(self, ability, getattr(self, ability) + amount)
        else:
            raise ValueError(f"Invalid ability score: {ability}")


class AbilityModifiers:
    def __init__(self, ability_scores: AbilityScores):
        self.might = self.calculate_modifier(ability_scores.might)
        self.reflexes = self.calculate_modifier(ability_scores.reflexes)
        self.endurance_core = self.calculate_modifier(ability_scores.endurance_core)
        self.arcane_logic = self.calculate_modifier(ability_scores.arcane_logic)
        self.aether_sense = self.calculate_modifier(ability_scores.aether_sense)
        self.presence = self.calculate_modifier(ability_scores.presence)

    def calculate_modifier(self, score: int) -> int:
        return (score - 10) // 2


class EquipmentProficiencies:
    def __init__(self, armor: list[str], weapons: list[str], tools: list[str]):
        self.armor = armor
        self.weapons = weapons
        self.tools = tools
        

class Skills:
    def __init__(self, skills: list[str], modifiers: AbilityModifiers, proficiency_modifier: int):
        self.skills = skills
        self.modifiers = modifiers
        self.proficiency_modifier = proficiency_modifier
        self.skills_info = self.load_skills_info()
        self.skill_scores = self.calculate_skill_scores()
    
    def load_skills_info(self):
        skills_path = Path('data/skills.json')
        with open(skills_path, 'r') as f:
            skills_info = json.load(f)
        return skills_info['skills']
    
    def calculate_skill_scores(self):
        skill_scores = {}
        for skill in self.skills:
            ability = self.get_ability_for_skills(skill)
            ability = ability.lower().replace(' ', '_')
            modifier = getattr(self.modifiers, ability)
            skill_scores[skill] = modifier + self.proficiency_modifier
        return skill_scores
    
    def get_ability_for_skills(self, skill: str) -> str:
        skill_info = next((s for s in self.skills_info if s['name'] == skill), None)
        if skill_info:
            return skill_info['ability']
        else:
            raise ValueError(f"Skill '{skill}' not found")


class Pack:
    def __init__(self, armor: list[dict[str, Union[int, int]]], weapons: list[dict[str, Union[int, int]]],
                 tools: list[dict[str, Union[str, int]]], potions: list[dict[str, Union[str, int]]],
                 currency: list[dict[str, int]], misc: list[str]):
        self.armor = armor
        self.weapons = weapons
        self.tools = tools
        self.potions = potions
        self.currency = currency
        self.misc = misc
        
        
class Equipped:
    def __init__(self, armor: dict[str, Union[str, int]], weapon: dict[str, Union[str, int]],
                 shield: dict[str, Union[str, int]], tools: list[dict[str, Union[str, int]]],
                 potions: list[dict[str, Union[str, int]]]):
        self.armor = armor
        self.weapon = weapon
        self.shield = shield
        self.tools = tools
        self.potions = potions
