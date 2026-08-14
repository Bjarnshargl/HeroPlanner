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
    class TEXT NOT NULL
);

CREATE TABLE hero_slots (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position INTEGER NOT NULL UNIQUE
);

CREATE TABLE runewords (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    item_type INTEGER NOT NULL,
    description TEXT,
    FOREIGN KEY (item_type) REFERENCES item_types(id)
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type INTEGER NOT NULL,
    item_class INTEGER,
    runeword_id INTEGER,
    ethereal BOOLEAN NOT NULL DEFAULT 0 CHECK (ethereal IN (0, 1)),
    url TEXT,
    FOREIGN KEY (type) REFERENCES item_types(id),
    FOREIGN KEY (item_class) REFERENCES item_classes(id),
    FOREIGN KEY (runeword_id) REFERENCES runewords(id)
);

CREATE TABLE runeword_runes (
    id INTEGER PRIMARY KEY,
    runeword_id INTEGER NOT NULL,
    rune_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    FOREIGN KEY (runeword_id) REFERENCES runewords(id),
    FOREIGN KEY (rune_id) REFERENCES runes(id),
    UNIQUE (runeword_id, position)
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