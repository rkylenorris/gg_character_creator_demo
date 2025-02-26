-- Table for NPCs (Non-Player Characters)
CREATE TABLE npcs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    role TEXT, -- Merchant, Quest Giver, Informant, etc.
    description TEXT,
    location TEXT, -- Where the NPC is found
    dialogue_start TEXT, -- Default starting dialogue
    trade_items TEXT -- JSON array of tradeable items
);

-- Table for NPC Dialogue Options
CREATE TABLE npc_dialogue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npc_id INTEGER,
    player_input TEXT, -- What the player says
    npc_response TEXT, -- NPC's reply
    next_dialogue_id INTEGER, -- Links to next dialogue node (or NULL for end)
    FOREIGN KEY (npc_id) REFERENCES npcs(id) ON DELETE CASCADE
);

-- Table for Monsters
CREATE TABLE monsters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    type TEXT CHECK (type IN ('Beast', 'Construct', 'Undead', 'Humanoid', 'Aberration', 'Elemental')),
    description TEXT,
    hit_points INTEGER NOT NULL,
    armor_class INTEGER NOT NULL,
    speed INTEGER,
    abilities TEXT, -- JSON array of special abilities
    resistances TEXT, -- JSON array of damage resistances
    weaknesses TEXT, -- JSON array of damage vulnerabilities
    loot_id INTEGER, -- Links to loot table
    FOREIGN KEY (loot_id) REFERENCES loot_tables(id) ON DELETE SET NULL
);

-- Table for Monster Abilities (linked to monsters)
CREATE TABLE monster_abilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monster_id INTEGER,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    effect TEXT, -- JSON describing effect (e.g., {"damage": "2d6", "type": "fire"})
    FOREIGN KEY (monster_id) REFERENCES monsters(id) ON DELETE CASCADE
);

-- Table for Loot Tables
CREATE TABLE loot_tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monster_id INTEGER,
    possible_drops TEXT, -- JSON array of item names and drop chances
    FOREIGN KEY (monster_id) REFERENCES monsters(id) ON DELETE CASCADE
);
