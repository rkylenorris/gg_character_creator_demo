from .character_info import Pack, Skills, EquipmentProficencies, AbilityScores, AbilityModifiers, HitPoints, Equiped
from .character_basis import CharacterClass, Race, Background

class CharacterSheet:
    
    name: str
    level: int = 1
    player_class: CharacterClass
    race: Race
    background: Background
    abilities: AbilityScores
    ability_modifiers: AbilityModifiers
    equipment_proficencies: EquipmentProficencies
    armor_class: int
    initiative: int
    hit_points: HitPoints
    appearance: str
    equiped: Equiped
    pack: Pack
    proficency_modifier: int
    skills: Skills
    
    def __init__(self, name: str, player_class: CharacterClass, race: Race,
                 background: Background, appearance: str):
        self.name = name
        self.player_class = player_class
        self.race = race
        self.background = background
        self.abilities = AbilityScores(starting_scores=player_class.starting_ability_scores)
        self.add_class_race_ability_increases()
        self.ability_modifiers = AbilityModifiers(self.abilities)
        self.proficency_modifier = 2 # increases by 1 at levels 5 and 8
        self.equipment_proficencies = self.get_equipment_proficencies()
        self.skills = self.get_skill_proficencies()
        self.equiped = None
        self.pack = None
        self.hit_points = HitPoints()
        self.hit_points.roll_hit_points(player_class.hit_die, self.abilities.endurance_core)
        self.appearance = appearance
    
    def add_class_race_ability_increases(self):
        
        for ability in self.player_class.primary_abilities:
            ability = ability.lower().replace(' ', '_')
            self.abilities.increase_ability_score(ability, 1)
        
        for ability, increase in self.race.ability_bonuses.items():
            ability = ability.lower().replace(' ', '_')
            self.abilities.increase_ability_score(ability, increase)
    
    def get_equipment_proficencies(self):
        armor = [item for item in self.player_class.proficiencies['armor']]
        weapons = [item for item in self.player_class.proficiencies['weapons']]
        tools = [item for item in self.player_class.proficiencies['tools']]
        
        for item in self.background.tool_proficiencies:
            tools.append(item)
        
        return EquipmentProficencies(armor, weapons, tools)
    
    def get_skill_proficencies(self):
        skills = [skill for skill in self.player_class.skills]
        for skill in self.background.skill_proficiencies:
            skills.append(skill)
        return Skills(skills, self.ability_modifiers, self.proficency_modifier)
    
    def __repr__(self):
        return f"{self.name} - {self.player_class.name} - {self.race.name} - {self.background.name}"


def character_creator(char_name: str, class_name: str, race_name: str, background_name: str, appearance: str):
    player_class = CharacterClass.load_class(class_name)
    race = Race.load_race(race_name)
    background = Background.load_background(background_name)
    return CharacterSheet(char_name, player_class, race, background, appearance)

    