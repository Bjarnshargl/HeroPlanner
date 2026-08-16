CREATE TABLE item_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE item_classes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE runes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    tier TEXT NOT NULL CHECK (tier IN ('low', 'mid', 'high'))
);

CREATE TABLE heroes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class_id INTEGER NOT NULL,
    FOREIGN KEY (class_id) REFERENCES hero_classes(id)
);

CREATE TABLE hero_classes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE mercenaries (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class_id INTEGER NOT NULL,
    FOREIGN KEY (class_id) REFERENCES merc_classes(id)
);

CREATE TABLE merc_classes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE hero_slots (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position INTEGER NOT NULL UNIQUE
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type INTEGER NOT NULL,
    item_class INTEGER,
    runeword_name TEXT,
    ethereal BOOLEAN NOT NULL DEFAULT 0 CHECK (ethereal IN (0, 1)),
    url TEXT,
    comment TEXT,
    FOREIGN KEY (type) REFERENCES item_types(id),
    FOREIGN KEY (item_class) REFERENCES item_classes(id)
);

CREATE TABLE runewords (
    name TEXT PRIMARY KEY,
    item_type INTEGER NOT NULL,
    description TEXT
);

CREATE TABLE runeword_runes (
    name TEXT NOT NULL,
    rune_id INTEGER NOT NULL,
    position INTEGER NOT NULL
);

CREATE TABLE hero_items (
    id INTEGER PRIMARY KEY,
    hero_id INTEGER NOT NULL,
    slot_id INTEGER NOT NULL,
    item_id INTEGER,
    collected BOOLEAN NOT NULL DEFAULT 0 CHECK (collected IN (0, 1)),
    FOREIGN KEY (hero_id) REFERENCES heroes(id),
    FOREIGN KEY (slot_id) REFERENCES hero_slots(id),
    FOREIGN KEY (item_id) REFERENCES items(id),
    UNIQUE (hero_id, slot_id)
);

CREATE TABLE merc_items (
    id INTEGER PRIMARY KEY,
    merc_id INTEGER NOT NULL,
    slot_id INTEGER NOT NULL,
    item_id INTEGER,
    collected BOOLEAN NOT NULL DEFAULT 0 CHECK (collected IN (0, 1)),
    FOREIGN KEY (merc_id) REFERENCES mercenaries(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

CREATE TABLE merc_slots (
    position INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL
);