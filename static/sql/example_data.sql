INSERT INTO mercenaries(id, name, class_id) VALUES
(1,'Wendy', 1),
(2,'Fiona', 1),
(3,'Emilio', 2),
(4,'Azrael', 2),
(5,'Flux', 3),
(6,'Scorch', 3),
(7,'Moo', 4),
(8,'Ulf', 5),
(9,'Wulf', 5);

INSERT INTO items(
    id,
    name,
    type,
    item_class,
    runeword_id,
    ethereal,
    url,
    comment
) VALUES (
          1,
          'Vampire Gaze',
          4,
          6,
          0,
          1,
          'https://diablo.fandom.com/wiki/Vampire_Gaze',
          'Socketed best with IAS charm'
         );

INSERT INTO runewords (
    name,
    item_type,
    description
    ) VALUES
    ('Exile', 2, 'Ethereal Sacred Targe with +35–45 All Resistances');

INSERT INTO runeword_runes (
    name,
    rune_id,
    position
    ) VALUES
    ('Exile', 26, 1),
    ('Exile', 27, 2),
    ('Exile', 24, 3),
    ('Exile', 14, 4);
