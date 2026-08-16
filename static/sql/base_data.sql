INSERT INTO runes (id, name, tier) VALUES (1, 'El', 'low');
INSERT INTO runes (id, name, tier) VALUES (2, 'Eld', 'low');
INSERT INTO runes (id, name, tier) VALUES (3, 'Tir', 'low');
INSERT INTO runes (id, name, tier) VALUES (4, 'Nef', 'low');
INSERT INTO runes (id, name, tier) VALUES (5, 'Eth', 'low');
INSERT INTO runes (id, name, tier) VALUES (6, 'Ith', 'low');
INSERT INTO runes (id, name, tier) VALUES (7, 'Tal', 'low');
INSERT INTO runes (id, name, tier) VALUES (8, 'Ort', 'low');
INSERT INTO runes (id, name, tier) VALUES (9, 'Thul', 'low');
INSERT INTO runes (id, name, tier) VALUES (10, 'Ral', 'low');
INSERT INTO runes (id, name, tier) VALUES (11, 'Shael', 'low');
INSERT INTO runes (id, name, tier) VALUES (12, 'Amn', 'low');
INSERT INTO runes (id, name, tier) VALUES (13, 'Sol', 'low');
INSERT INTO runes (id, name, tier) VALUES (14, 'Dol', 'low');
INSERT INTO runes (id, name, tier) VALUES (15, 'Hel', 'low');
INSERT INTO runes (id, name, tier) VALUES (16, 'Io', 'low');
INSERT INTO runes (id, name, tier) VALUES (17, 'Lum', 'low');
INSERT INTO runes (id, name, tier) VALUES (18, 'Ko', 'low');
INSERT INTO runes (id, name, tier) VALUES (19, 'Fal', 'low');
INSERT INTO runes (id, name, tier) VALUES (20, 'Lem', 'low');
INSERT INTO runes (id, name, tier) VALUES (21, 'Pul', 'low');
INSERT INTO runes (id, name, tier) VALUES (22, 'Um', 'mid');
INSERT INTO runes (id, name, tier) VALUES (23, 'Mal', 'mid');
INSERT INTO runes (id, name, tier) VALUES (24, 'Ist', 'mid');
INSERT INTO runes (id, name, tier) VALUES (25, 'Gul', 'mid');
INSERT INTO runes (id, name, tier) VALUES (26, 'Vex', 'high');
INSERT INTO runes (id, name, tier) VALUES (27, 'Ohm', 'high');
INSERT INTO runes (id, name, tier) VALUES (28, 'Lo', 'high');
INSERT INTO runes (id, name, tier) VALUES (29, 'Sur', 'high');
INSERT INTO runes (id, name, tier) VALUES (30, 'Ber', 'high');
INSERT INTO runes (id, name, tier) VALUES (31, 'Jah', 'high');
INSERT INTO runes (id, name, tier) VALUES (32, 'Cham', 'high');
INSERT INTO runes (id, name, tier) VALUES (33, 'Zod', 'high');

INSERT INTO item_classes (id, name) VALUES
(1, 'Base'),
(2, 'Normal'),
(3, 'Magic'),
(4, 'Rare'),
(5, 'Crafted'),
(6, 'Unique'),
(7, 'Set'),
(8, 'Runeword');

INSERT INTO item_types(id, name) VALUES
(1, 'Weapon'),
(2, 'Shield'),
(3, 'Breastplate'),
(4, 'Helmet'),
(5, 'Gloves'),
(6, 'Belt'),
(7, 'Boots'),
(8, 'Necklace'),
(9, 'Ring'),
(10, 'None');

INSERT INTO merc_classes(id, name) VALUES
(1,'Act I Rogue'),
(2,'Act II Desert Mercenary'),
(3,'Act III Iron Wolf'),
(4,'Act IV Cow King'),
(5,'Act V Barbarian');

INSERT INTO hero_classes(id, name) VALUES
(1, 'Amazon'),
(2, 'Asassin'),
(3, 'Barbarian'),
(4, 'Druid'),
(5, 'Necromancer'),
(6, 'Paladin'),
(7, 'Sorceress'),
(8, 'Warlock');

INSERT INTO hero_slots(id, name, position) VALUES
(1, 'Main Hand', 1),
(2, 'Offhand', 2),
(3, 'Breastplate', 3),
(4, 'Helmet', 4);

SELECT
	m.id AS merc_id,
	m.name as merc_name,
	m.class_id AS merc_class_id,
	mi.slot_id as merc_slot_id,
	mi.item_id AS merc_item_id,
	i.name AS merc_item_name,
	mi.collected AS merc_item_collected
FROM mercenaries m
JOIN merc_items mi
ON mi.merc_id = m.id
JOIN items i
on mi.item_id = i.id
JOIN merc_classes mc
ON m.class_id = mc.id;


INSERT INTO merc_slots (position, name)
VALUES
(1, 'Mainhand'),
(2, 'Offhand'),
(3, 'Breastplate'),
(4, 'Helmet');
