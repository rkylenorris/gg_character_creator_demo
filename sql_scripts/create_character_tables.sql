CREATE TABLE races (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    ability_score_increase TEXT, -- JSON format: {"Might": 2, "Endurance Core": 1}
    size TEXT CHECK (size IN ('Small', 'Medium', 'Large')),
    speed INTEGER,
    traits TEXT, -- JSON array of traits
    languages TEXT -- JSON array of languages
);

CREATE TABLE backgrounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    feature_name TEXT,
    feature_description TEXT,
    skill_proficiencies TEXT, -- JSON array of skills
    tool_proficiencies TEXT, -- JSON array of tools
    starting_equipment TEXT -- JSON array of starting items
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    hit_die TEXT NOT NULL,
    primary_abilities TEXT, -- JSON array of primary abilities
    saving_throws TEXT, -- JSON array of saving throws
    proficiencies TEXT, -- JSON format: {"armor": [], "weapons": [], "tools": []}
    skills TEXT, -- JSON array of class skills
    starting_equipment TEXT, -- JSON array of items
    starting_ability_scores TEXT -- JSON format: {"Might": 14, "Reflexes": 12}
);

CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    ability TEXT NOT NULL CHECK (ability IN ('Might', 'Reflexes', 'Endurance Core', 'Arcane Logic', 'Aether Sense', 'Presence')),
    description TEXT NOT NULL
);

CREATE TABLE skill_proficiency_levels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_id INTEGER,
    level TEXT CHECK (level IN ('Novice', 'Expert', 'Mastery')),
    effect TEXT NOT NULL,
    FOREIGN KEY (skill_id) REFERENCES skills(id) ON DELETE CASCADE
);

CREATE TABLE weapons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    type TEXT CHECK (type IN ('One-Handed', 'Two-Handed', 'Finesse', 'Light', 'Utility')),
    damage TEXT NOT NULL,
    damage_type TEXT CHECK (damage_type IN ('Slashing', 'Bludgeoning', 'Piercing', 'Electric', 'Force')),
    special TEXT -- Additional unique effects
);

CREATE TABLE armor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    type TEXT CHECK (type IN ('Light Armor', 'Medium Armor', 'Heavy Armor', 'Shield')),
    armor_class INTEGER NOT NULL,
    special TEXT -- Unique properties
);

CREATE TABLE gadgets_tools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    effect TEXT NOT NULL,
    uses TEXT -- JSON format describing specific uses
);

CREATE TABLE consumables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    effect TEXT NOT NULL,
    uses TEXT -- JSON format describing how the consumable is used
);
