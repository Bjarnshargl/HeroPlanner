from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///instance/hero.db")


# Test

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")


@app.route('/hero')
def hero():  # put application's code here
    return render_template("hero.html")


@app.route("/show_runes")
def show_runes():
    return render_template("show_runes.html")


@app.route("/show_items", methods=["GET", "POST"])
def show_items():
    items = db.execute("""SELECT i.id,
                                 i.name,
                                 it.name as type,
                                 ic.name as item_class,
                                 i.runeword_name,
                                 i.ethereal,
                                 i.url,
                                 i.comment
                          FROM items i
                                   JOIN item_types it ON it.id = i.type
                                   JOIN item_classes ic ON ic.id = i.item_class
                          ORDER BY i.type, i.name;""")

    if request.method == "POST":
        item_id = str(request.form.get("item_id"))
        print("ITEM_ID: " + str(item_id))

        if item_id:
            items = db.execute("""SELECT i.id,
                                             i.name,
                                             it.name as type,
                                             ic.name as item_class,
                                             i.runeword_name,
                                             i.ethereal,
                                             i.url,
                                             i.comment
                                      FROM items i
                                               JOIN item_types it ON it.id = i.type
                                               JOIN item_classes ic ON ic.id = i.item_class
                                      WHERE i.id = ?
                                      ORDER BY i.type, i.name;""", item_id)

    return render_template("show_items.html", items=items)


@app.route("/create_items", methods=["GET", "POST"])
def create_items():
    item_types = db.execute("SELECT id, name FROM item_types ORDER BY name ASC;")
    item_classes = db.execute("SELECT id, name FROM item_classes ORDER BY name ASC;")
    runewords = db.execute("SELECT name FROM runewords ORDER BY name ASC;")

    if request.method == "POST":
        name = str(request.form.get("name"))
        item_type = request.form.get("item_type")
        item_class = request.form.get("item_class")
        runeword_name = request.form.get("runeword") or None
        ethereal = request.form.get("ethereal")
        url = request.form.get("url")
        comment = request.form.get("comment")

        if name and item_type and item_class and ethereal:
            if not url:
                url = "no URL"
            if not comment:
                comment = "no comment"

        db.execute(
            """
            INSERT INTO items
                (name, type, item_class, runeword_name, ethereal, url, comment)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, name, item_type, item_class, runeword_name, ethereal, url, comment
        )

        return render_template("create_items.html", item_types=item_types, item_classes=item_classes,
                               runewords=runewords)

    else:
        return render_template("create_items.html", item_types=item_types, item_classes=item_classes,
                               runewords=runewords)


@app.route("/delete_items", methods=["GET", "POST"])
def delete_items():
    items = db.execute("SELECT name FROM items;")

    if request.method == "POST":
        name = str(request.form.get("name"))

        db.execute("DELETE FROM items WHERE name = ?", name)

        return render_template("delete_items.html", items=items)

    else:
        runewords = db.execute("SELECT name FROM runewords;")
        return render_template("delete_items.html", items=items)


@app.route("/show_merc", methods=["GET", "POST"])
def show_merc():
    img = None
    mercenaries = db.execute("""
    SELECT
        m.id AS merc_id, 
        m.name as merc_name, 
        m.class_id AS merc_class_id, 
        mi.slot_id as merc_slot_id,
        ms.name as merc_slot_name, 
        mi.item_id AS merc_item_id, 
        i.name AS merc_item_name, 
        mi.collected AS merc_item_collected
    FROM mercenaries m
    JOIN merc_items mi
    ON mi.merc_id = m.id
    JOIN items i
    on mi.item_id = i.id
    JOIN merc_classes mc
    ON m.class_id = mc.id
    JOIN merc_slots ms
    ON ms.position = mi.slot_id;
    """)
    merc_names = db.execute("SELECT id, name FROM mercenaries;")
    if request.method == "POST":
        name = str(request.form.get("name"))

        if name:
            mercenaries = db.execute("""
            SELECT
                m.id AS merc_id, 
                m.name as merc_name, 
                m.class_id AS merc_class_id, 
                mi.slot_id as merc_slot_id,
                ms.name as merc_slot_name, 
                mi.item_id AS merc_item_id, 
                i.name AS merc_item_name, 
                mi.collected AS merc_item_collected
            FROM mercenaries m
            JOIN merc_items mi
            ON mi.merc_id = m.id
            JOIN items i
            on mi.item_id = i.id
            JOIN merc_classes mc
            ON m.class_id = mc.id
            JOIN merc_slots ms
            ON ms.position = mi.slot_id
            WHERE m.id = ?;
            """, name)

            match name:
                case "1":
                    img = "images/hero/a1rogue.png"
                case "2":
                    img = "images/hero/a2desert.png"
                case "3":
                    img = "images/hero/a3iron.png"
                case "4":
                    img = "images/hero/a4ck.png"
                case "5":
                    img = "images/hero/a5barb.png"

            print(name)
            print(img)
            return render_template("show_merc.html", mercenaries=mercenaries, merc_names=merc_names, img=img)

    return render_template("show_merc.html", mercenaries=mercenaries, merc_names=merc_names, img=img)


@app.route("/edit_merc", methods=["GET", "POST"])
def edit_merc():
    img = None
    mercenaries = db.execute("""
    SELECT
        m.id AS merc_id, 
        m.name as merc_name, 
        m.class_id AS merc_class_id, 
        mi.slot_id as merc_slot_id,
        ms.name as merc_slot_name, 
        mi.item_id AS merc_item_id, 
        i.name AS merc_item_name, 
        mi.collected AS merc_item_collected
    FROM mercenaries m
    JOIN merc_items mi
    ON mi.merc_id = m.id
    JOIN items i
    on mi.item_id = i.id
    JOIN merc_classes mc
    ON m.class_id = mc.id
    JOIN merc_slots ms
    ON ms.position = mi.slot_id;
    """)
    merc_names = db.execute("SELECT id, name FROM mercenaries;")
    if request.method == "POST":
        merc_id = request.form.get("name")
        print(merc_id)

        if merc_id:
            merc_class = db.execute("SELECT class_id FROM mercenaries WHERE id = ?;", int(merc_id))[0]['class_id']
            mercenaries = db.execute("""
            SELECT
                m.id AS merc_id, 
                m.name as merc_name, 
                m.class_id AS merc_class_id, 
                mi.slot_id as merc_slot_id,
                ms.name as merc_slot_name, 
                mi.item_id AS merc_item_id, 
                i.name AS merc_item_name, 
                mi.collected AS merc_item_collected
            FROM mercenaries m
            JOIN merc_items mi
            ON mi.merc_id = m.id
            JOIN items i
            on mi.item_id = i.id
            JOIN merc_classes mc
            ON m.class_id = mc.id
            JOIN merc_slots ms
            ON ms.position = mi.slot_id
            WHERE m.id = ?;
            """, int(merc_id))

            match str(merc_class):
                case "1":
                    img = "images/hero/a1rogue.png"
                case "2":
                    img = "images/hero/a2desert.png"
                case "3":
                    img = "images/hero/a3iron.png"
                case "4":
                    img = "images/hero/a4ck.png"
                case "5":
                    img = "images/hero/a5barb.png"

            collected_1 = request.form.get("collected_1")
            collected_2 = request.form.get("collected_2")
            collected_3 = request.form.get("collected_3")
            collected_4 = request.form.get("collected_4")

            print("MERC_ID: " + str(merc_id))
            print("MERC_CLASS: " + str(merc_class))
            print("COLLECTED_1: " + str(collected_1))
            print("COLLECTED_2: " + str(collected_2))
            print("COLLECTED_3: " + str(collected_3))
            print("COLLECTED_4: " + str(collected_4))

            if collected_1 and collected_2 and collected_3 and collected_4:
                collected_1 = int(collected_1)
                collected_2 = int(collected_2)
                collected_3 = int(collected_3)
                collected_4 = int(collected_4)
                print("MERC_ID: " + str(merc_id))
                print("MERC_CLASS: " + str(merc_class))
                db.execute("UPDATE merc_items SET collected = ? WHERE merc_id = ? AND slot_id = 1; ", collected_1,
                           int(merc_id))
                db.execute("UPDATE merc_items SET collected = ? WHERE merc_id = ? AND slot_id = 2; ", collected_2,
                           int(merc_id))
                db.execute("UPDATE merc_items SET collected = ? WHERE merc_id = ? AND slot_id = 3; ", collected_3,
                           int(merc_id))
                db.execute("UPDATE merc_items SET collected = ? WHERE merc_id = ? AND slot_id = 4; ", collected_4,
                           int(merc_id))

            return render_template("edit_merc.html", mercenaries=mercenaries, merc_names=merc_names, img=img,
                                   merc_id=merc_id)

    return render_template("edit_merc.html", mercenaries=mercenaries, merc_names=merc_names, img=img)


@app.route("/create_merc", methods=["GET", "POST"])
def create_merc():
    merc_classes = db.execute("SELECT id, name FROM merc_classes;")
    mainhands = db.execute("SELECT id, name FROM items WHERE TYPE=1;")
    offhands = db.execute("SELECT id, name FROM items WHERE TYPE=2;")
    breastplates = db.execute("SELECT id, name FROM items WHERE TYPE=3;")
    helmets = db.execute("SELECT id, name FROM items WHERE TYPE=4;")

    if request.method == "POST":
        # name merc_class item_1 item_2 item_3 item_4
        name = str(request.form.get("name"))
        merc_class = str(request.form.get("merc_class"))
        item_1 = str(request.form.get("item_1"))
        item_2 = str(request.form.get("item_2"))
        item_3 = str(request.form.get("item_3"))
        item_4 = str(request.form.get("item_4"))
        collected_1 = str(request.form.get("collected_1"))
        collected_2 = str(request.form.get("collected_2"))
        collected_3 = str(request.form.get("collected_3"))
        collected_4 = str(request.form.get("collected_4"))

        if name and merc_class and item_1 and item_2 and item_3 and item_4 and collected_1 and collected_2 and collected_3 and collected_4:
            db_name = db.execute("SELECT id FROM mercenaries WHERE UPPER(name) = UPPER(?);", name)
            if len(db_name) == 0:
                db.execute("INSERT INTO mercenaries (name, class_id) VALUES (?, ?);", name, merc_class)
                merc_id = db.execute("SELECT id FROM mercenaries WHERE name = ?;", name)[0]['id']
                db.execute("INSERT INTO merc_items (merc_id, slot_id, item_id, collected) VALUES (?, 1, ?, ?);",
                           merc_id, item_1, collected_1)
                db.execute("INSERT INTO merc_items (merc_id, slot_id, item_id, collected) VALUES (?, 2, ?, ?);",
                           merc_id, item_2, collected_2)
                db.execute("INSERT INTO merc_items (merc_id, slot_id, item_id, collected) VALUES (?, 3, ?, ?);",
                           merc_id, item_3, collected_3)
                db.execute("INSERT INTO merc_items (merc_id, slot_id, item_id, collected) VALUES (?, 4, ?, ?);",
                           merc_id, item_4, collected_4)
                return render_template("created_merc.html")
            else:
                return render_template("sorry.html", message=name + " already exists.")

        return render_template("create_merc.html", merc_classes=merc_classes, mainhands=mainhands, offhands=offhands,
                               breastplates=breastplates, helmets=helmets)

    return render_template("create_merc.html", merc_classes=merc_classes, mainhands=mainhands, offhands=offhands,
                           breastplates=breastplates, helmets=helmets)


@app.route("/delete_merc", methods=["GET", "POST"])
def delete_merc():
    img = None
    mercenaries = db.execute("""
    SELECT
        m.id AS merc_id, 
        m.name as merc_name, 
        m.class_id AS merc_class_id, 
        mi.slot_id as merc_slot_id,
        ms.name as merc_slot_name, 
        mi.item_id AS merc_item_id, 
        i.name AS merc_item_name, 
        mi.collected AS merc_item_collected
    FROM mercenaries m
    JOIN merc_items mi
    ON mi.merc_id = m.id
    JOIN items i
    on mi.item_id = i.id
    JOIN merc_classes mc
    ON m.class_id = mc.id
    JOIN merc_slots ms
    ON ms.position = mi.slot_id;
    """)
    merc_names = db.execute("SELECT id, name FROM mercenaries;")
    if request.method == "POST":
        merc_id = request.form.get("name")
        print("MERC_ID: " + str(merc_id))

        if merc_id:
            delete_merc_id = request.form.get("delete_merc_id")
            merc_class = db.execute("SELECT class_id FROM mercenaries WHERE id = ?;", int(merc_id))[0]['class_id']
            mercenaries = db.execute("""
            SELECT
                m.id AS merc_id, 
                m.name as merc_name, 
                m.class_id AS merc_class_id, 
                mi.slot_id as merc_slot_id,
                ms.name as merc_slot_name, 
                mi.item_id AS merc_item_id, 
                i.name AS merc_item_name, 
                mi.collected AS merc_item_collected
            FROM mercenaries m
            JOIN merc_items mi
            ON mi.merc_id = m.id
            JOIN items i
            on mi.item_id = i.id
            JOIN merc_classes mc
            ON m.class_id = mc.id
            JOIN merc_slots ms
            ON ms.position = mi.slot_id
            WHERE m.id = ?;
            """, int(merc_id))
            print("MERC_CLASS: " + str(merc_class))
            print("MERC_DELETE: " + str(delete_merc_id))

            match str(merc_class):
                case "1":
                    img = "images/hero/a1rogue.png"
                case "2":
                    img = "images/hero/a2desert.png"
                case "3":
                    img = "images/hero/a3iron.png"
                case "4":
                    img = "images/hero/a4ck.png"
                case "5":
                    img = "images/hero/a5barb.png"

            if delete_merc_id:
                db.execute("DELETE FROM merc_items WHERE merc_id = ?;", int(delete_merc_id))
                db.execute("DELETE FROM mercenaries WHERE id = ?;", int(delete_merc_id))
                return render_template("deleted_merc.html")

        return render_template("delete_merc.html", mercenaries=mercenaries, merc_names=merc_names, img=img,
                               merc_id=merc_id)

    return render_template("delete_merc.html", mercenaries=mercenaries, merc_names=merc_names, img=img)


@app.route("/show_hero", methods=["GET", "POST"])
def show_hero():
    img = None
    heroes = db.execute("""
        SELECT
            h.id AS hero_id,
            h.name AS hero_name,
            hc.name AS hero_class,
            i.name AS item_name,
            hs.name AS slot,
            i.runeword_name AS runeword_name,
            i.ethereal AS ethereal,
            i.url AS url,
            i.comment AS comment,
            hi.collected AS collected
        FROM hero_items hi
        JOIN heroes h ON hi.hero_id = h.name
        JOIN hero_slots hs ON hi.slot_id = hs.position
        JOIN items i ON i.id = hi.item_id
        JOIN hero_classes hc ON hc.id = h.class_id;
    """)
    hero_names = db.execute("SELECT id, name FROM heroes;")
    if request.method == "POST":
        hero_id = str(request.form.get("name"))
        print("HERO_ID: " + str(hero_id))

        hero_class = db.execute("SELECT class_id FROM heroes WHERE id = ?;", int(hero_id))[0]['class_id']
        print("HERO_CLASS: " + str(hero_class))

        if hero_id:
            heroes = db.execute("""
                SELECT
                    h.id AS hero_id,
                    h.name AS hero_name,
                    hc.name AS hero_class,
                    i.name AS item_name,
                    hs.name AS slot,
                    i.runeword_name AS runeword_name,
                    i.ethereal AS ethereal,
                    i.url AS url,
                    i.comment AS comment,
                    hi.collected AS collected
                FROM hero_items hi 
                JOIN heroes h ON hi.hero_id = h.name
                JOIN hero_slots hs ON hi.slot_id = hs.position
                JOIN items i ON i.id = hi.item_id
                JOIN hero_classes hc ON hc.id = h.class_id
                WHERE h.id = ?; 
            """, int(hero_id))

            if hero_class:
                match str(hero_class):
                    case "1":
                        img = "images/classes/amazon.png"
                    case "2":
                        img = "images/classes/assasin.png"
                    case "3":
                        img = "images/classes/Barbarian.png"
                    case "4":
                        img = "images/classes/Druid.png"
                    case "5":
                        img = "images/classes/Necromancer.png"
                    case "6":
                        img = "images/classes/Paladin.png"
                    case "7":
                        img = "images/classes/Sorceress.png"
                    case "8":
                        img = "images/classes/Warlock.png"
            print(img)
            return render_template("show_hero.html", heroes=heroes, hero_names=hero_names, img=img)

    return render_template("show_hero.html", heroes=heroes, hero_names=hero_names, img=img)


@app.route("/edit_hero", methods=["GET", "POST"])
def edit_hero():
    img = None
    heroes = db.execute("""
        SELECT
            h.id AS hero_id,
            h.name AS hero_name,
            hc.name AS hero_class,
            i.name AS item_name,
            hs.name AS slot,
            i.runeword_name AS runeword_name,
            i.ethereal AS ethereal,
            i.url AS url,
            i.comment AS comment,
            hi.collected AS collected
        FROM hero_items hi
        JOIN heroes h ON hi.hero_id = h.name
        JOIN hero_slots hs ON hi.slot_id = hs.position
        JOIN items i ON i.id = hi.item_id
        JOIN hero_classes hc ON hc.id = h.class_id;
    """)
    hero_names = db.execute("SELECT id, name FROM heroes;")

    if request.method == "POST":
        hero_id = request.form.get("name")
        print("HERO_ID: " + str(hero_id))

        if hero_id:
            hero_id = int(hero_id)
            hero_class = db.execute("SELECT class_id FROM heroes WHERE id = ?;", hero_id)[0]['class_id']
            print("HERO_CLASS: " + str(hero_class))

            heroes = db.execute("""
                SELECT
                    h.id AS hero_id,
                    h.name AS hero_name,
                    hc.name AS hero_class,
                    i.name AS item_name,
                    hs.name AS slot,
                    i.runeword_name AS runeword_name,
                    i.ethereal AS ethereal,
                    i.url AS url,
                    i.comment AS comment,
                    hi.collected AS collected
                FROM hero_items hi
                JOIN heroes h ON hi.hero_id = h.name
                JOIN hero_slots hs ON hi.slot_id = hs.position
                JOIN items i ON i.id = hi.item_id
                JOIN hero_classes hc ON hc.id = h.class_id
                WHERE h.id = ?;
            """, int(hero_id))

            if hero_class:
                match str(hero_class):
                    case "1":
                        img = "images/classes/amazon.png"
                    case "2":
                        img = "images/classes/assasin.png"
                    case "3":
                        img = "images/classes/Barbarian.png"
                    case "4":
                        img = "images/classes/Druid.png"
                    case "5":
                        img = "images/classes/Necromancer.png"
                    case "6":
                        img = "images/classes/Paladin.png"
                    case "7":
                        img = "images/classes/Sorceress.png"
                    case "8":
                        img = "images/classes/Warlock.png"

            collected_1 = request.form.get("collected_1")
            collected_2 = request.form.get("collected_2")
            collected_3 = request.form.get("collected_3")
            collected_4 = request.form.get("collected_4")
            collected_5 = request.form.get("collected_5")
            collected_6 = request.form.get("collected_6")
            collected_7 = request.form.get("collected_7")
            collected_8 = request.form.get("collected_8")
            collected_9 = request.form.get("collected_9")
            collected_10 = request.form.get("collected_10")
            collected_11 = request.form.get("collected_11")
            collected_12 = request.form.get("collected_12")

            print("COLLECTED_1: " + str(collected_1))

            if collected_1 and collected_2 and collected_3 and collected_4 and collected_5 and collected_6 and collected_7 and collected_8 and collected_9 and collected_10 and collected_11 and collected_12:
                collected_1 = int(collected_1)
                collected_2 = int(collected_2)
                collected_3 = int(collected_3)
                collected_4 = int(collected_4)
                collected_5 = int(collected_5)
                collected_6 = int(collected_6)
                collected_7 = int(collected_7)
                collected_8 = int(collected_8)
                collected_9 = int(collected_9)
                collected_10 = int(collected_10)
                collected_11 = int(collected_11)
                collected_12 = int(collected_12)

                print("2 HERO_ID: " + str(hero_id))
                print("2 HERO_CLASS: " + str(hero_class))

                hero_name = db.execute("SELECT name FROM heroes WHERE id = ?;", hero_id)[0]['name']
                # hero_name = request.form.get("name")
                print("2 HERO_NAME: " + str(hero_name))

                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 1; ", collected_1,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 2; ", collected_2,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 3; ", collected_3,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 4; ", collected_4,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 5; ", collected_5,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 6; ", collected_6,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 7; ", collected_7,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 8; ", collected_8,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 9; ", collected_9,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 10; ", collected_10,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 11; ", collected_11,
                           hero_name)
                db.execute("UPDATE hero_items SET collected = ? WHERE hero_id = ? AND slot_id = 12; ", collected_12,
                           hero_name)

            return render_template("edit_hero.html", heroes=heroes, hero_names=hero_names, img=img, hero_id=hero_id)

    return render_template("edit_hero.html", heroes=heroes, hero_names=hero_names, img=img)


@app.route("/create_hero", methods=["GET", "POST"])
def create_hero():
    hero_classes = db.execute("SELECT id, name FROM hero_classes;")
    mainhands = db.execute("SELECT id, name FROM items WHERE TYPE=1;")
    offhands = db.execute("SELECT id, name FROM items WHERE TYPE=2;")
    breastplates = db.execute("SELECT id, name FROM items WHERE TYPE=3;")
    helmets = db.execute("SELECT id, name FROM items WHERE TYPE=4;")
    gloves = db.execute("SELECT id, name FROM items WHERE TYPE=5;")
    belts = db.execute("SELECT id, name FROM items WHERE TYPE=6;")
    boots = db.execute("SELECT id, name FROM items WHERE TYPE=7;")
    necklaces = db.execute("SELECT id, name FROM items WHERE TYPE=8;")
    rings = db.execute("SELECT id, name FROM items WHERE TYPE=9;")
    miscellaneous = db.execute("SELECT id, name FROM items WHERE TYPE=10;")

    if request.method == "POST":
        name = str(request.form.get("name"))
        hero_class = str(request.form.get("hero_class"))

        item_1 = str(request.form.get("item_1"))
        item_2 = str(request.form.get("item_2"))
        item_3 = str(request.form.get("item_3"))
        item_4 = str(request.form.get("item_4"))
        item_5 = str(request.form.get("item_5"))
        item_6 = str(request.form.get("item_6"))
        item_7 = str(request.form.get("item_7"))
        item_8 = str(request.form.get("item_8"))
        item_9 = str(request.form.get("item_9"))
        item_10 = str(request.form.get("item_10"))
        item_11 = str(request.form.get("item_11"))
        item_12 = str(request.form.get("item_12"))

        collected_1 = str(request.form.get("collected_1"))
        collected_2 = str(request.form.get("collected_2"))
        collected_3 = str(request.form.get("collected_3"))
        collected_4 = str(request.form.get("collected_4"))
        collected_5 = str(request.form.get("collected_1"))
        collected_6 = str(request.form.get("collected_2"))
        collected_7 = str(request.form.get("collected_3"))
        collected_8 = str(request.form.get("collected_4"))
        collected_9 = str(request.form.get("collected_1"))
        collected_10 = str(request.form.get("collected_2"))
        collected_11 = str(request.form.get("collected_3"))
        collected_12 = str(request.form.get("collected_4"))

        print("ITEMS:")
        print(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12)

        if (name and hero_class and item_1 and item_2 and item_3 and item_4 and item_5 and item_6 and item_7 and item_8
                and item_9 and item_10 and item_11 and item_12 and collected_1 and collected_2 and collected_3
                and collected_4 and collected_5 and collected_6 and collected_7 and collected_8 and collected_9
                and collected_10 and collected_11 and collected_12):

            db_name = db.execute("SELECT id FROM heroes WHERE UPPER(name) = UPPER(?);", name)
            if len(db_name) == 0:

                # Hero:
                db.execute("INSERT INTO heroes (name, class_id) VALUES(?, ?)", name, hero_class)

                # Hero items:
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 1, ?, ?)",
                           name, item_1, collected_1)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 2, ?, ?)",
                           name, item_2, collected_2)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 3, ?, ?)",
                           name, item_3, collected_3)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 4, ?, ?)",
                           name, item_4, collected_4)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 5, ?, ?)",
                           name, item_5, collected_5)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 6, ?, ?)",
                           name, item_6, collected_6)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 7, ?, ?)",
                           name, item_7, collected_7)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 8, ?, ?)",
                           name, item_8, collected_8)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 9, ?, ?)",
                           name, item_9, collected_9)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 10, ?, ?)",
                           name, item_10, collected_10)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 11, ?, ?)",
                           name, item_11, collected_11)
                db.execute("INSERT into hero_items (hero_id, slot_id, item_id, collected) VALUES(?, 12, ?, ?)",
                           name, item_12, collected_12)

                return render_template("created_hero.html")
            else:
                return render_template("sorry.html", message=name + " already exists.")

        return render_template("create_hero.html", mainhands=mainhands, offhands=offhands,
                               breastplates=breastplates, helmets=helmets, gloves=gloves, belts=belts, boots=boots,
                               necklaces=necklaces, rings=rings, miscellaneous=miscellaneous, hero_classes=hero_classes)

    return render_template("create_hero.html", mainhands=mainhands, offhands=offhands,
                           breastplates=breastplates, helmets=helmets, gloves=gloves, belts=belts, boots=boots,
                           necklaces=necklaces, rings=rings, miscellaneous=miscellaneous, hero_classes=hero_classes)


@app.route("/delete_hero", methods=["GET", "POST"])
def delete_hero():
    img = None
    heroes = db.execute("""
        SELECT h.name AS hero_name, c.name AS hero_class
        FROM heroes h JOIN hero_classes c ON h.class_id = c.id;
    """)
    hero_names = db.execute("SELECT id, name FROM heroes;")

    if request.method == "POST":
        hero_name = request.form.get("name")
        print("HERO_ID: " + str(hero_name))

        if hero_name:
            hero_class = db.execute("SELECT class_id FROM heroes WHERE name = ?;", hero_name)[0]['class_id']
            print("HERO_CLASS: " + str(hero_class))

            heroes = db.execute("""
                SELECT h.id AS hero_id, h.name AS hero_name, c.name AS hero_class
                FROM heroes h JOIN hero_classes c ON h.class_id = c.id
                WHERE h.name = ?;
            """, hero_name)

            if hero_class:
                match str(hero_class):
                    case "1":
                        img = "images/classes/amazon.png"
                    case "2":
                        img = "images/classes/assasin.png"
                    case "3":
                        img = "images/classes/Barbarian.png"
                    case "4":
                        img = "images/classes/Druid.png"
                    case "5":
                        img = "images/classes/Necromancer.png"
                    case "6":
                        img = "images/classes/Paladin.png"
                    case "7":
                        img = "images/classes/Sorceress.png"
                    case "8":
                        img = "images/classes/Warlock.png"

                delete_hero_name = request.form.get("delete_hero_name")
                print("DELETE_HERO_NAME: " + str(delete_hero_name))

                if delete_hero_name:
                    db.execute("DELETE FROM hero_items where hero_id = ?;", delete_hero_name)
                    db.execute("DELETE FROM heroes where name = ?;", delete_hero_name)
                    return render_template("deleted_hero.html")

            return render_template("delete_hero.html", heroes=heroes, hero_names=hero_names, img=img, hero_name=hero_name)

    return render_template("delete_hero.html", heroes=heroes, hero_names=hero_names, img=img)


@app.route("/show_runewords", methods=["GET", "POST"])
def show_runewords():
    runeword_names = db.execute("SELECT DISTINCT name FROM runeword_runes;")
    runewords = db.execute("""
                           SELECT rw.name AS runeword_name,
                                  rw.description,
                                  rr.rune_id,
                                  rr.position,
                                  r.name  AS rune_name,
                                  r.tier,
                                  it.name as item_type
                           FROM runewords rw
                                    JOIN runeword_runes rr
                                         ON rw.name = rr.name
                                    JOIN runes r
                                         ON r.id = rr.rune_id
                                    JOIN item_types it
                                         ON it.id = rw.item_type
                           ORDER BY rw.name, rr.position;""")

    if request.method == "POST":
        runeword_name = str(request.form.get("runeword_name"))
        print("RUNEWORD_ID: " + str(runeword_name))
        runewords = db.execute("""
                                   SELECT rw.name AS runeword_name,
                                          rw.description,
                                          rr.rune_id,
                                          rr.position,
                                          r.name  AS rune_name,
                                          r.tier,
                                          it.name as item_type
                                   FROM runewords rw
                                            JOIN runeword_runes rr
                                                 ON rw.name = rr.name
                                            JOIN runes r
                                                 ON r.id = rr.rune_id
                                            JOIN item_types it
                                                 ON it.id = rw.item_type
                                   WHERE rw.name = ?
                                   ORDER BY rw.name, rr.position;""", runeword_name)

    return render_template("show_runewords.html", runewords=runewords, runeword_names=runeword_names)


@app.route("/create_runewords", methods=["GET", "POST"])
def create_runewords():
    item_types = db.execute("SELECT id, name FROM item_types ORDER BY name ASC;")

    runes = db.execute("SELECT id, name, tier FROM runes;")
    runewords = db.execute("SELECT name FROM runewords;")

    if request.method == "POST":
        # This is the runewords part:

        name = str(request.form.get("name"))
        item_type_id = request.form.get("item_type_id")
        description = request.form.get("description")

        db_name = db.execute("SELECT name FROM runewords WHERE name = ?", name)
        print(db_name)

        if name is not None and item_type_id is not None and description is not None:
            if db_name != name:
                db.execute("INSERT INTO runewords (name, item_type, description) VALUES (?, ?, ?)", name, item_type_id,
                           description)
            else:
                print("runeword already exists")

        # Here comes the runeword runes part:

        rw_name = str(request.form.get("rw_name"))
        rune_id_1 = request.form.get("rune_id_1")
        rune_id_2 = request.form.get("rune_id_2")
        rune_id_3 = request.form.get("rune_id_3")
        rune_id_4 = request.form.get("rune_id_4")
        rune_id_5 = request.form.get("rune_id_5")
        rune_id_6 = request.form.get("rune_id_6")

        if rw_name is not None:
            if rune_id_1 is not None:
                db.execute("INSERT INTO runeword_runes (name, rune_id, position) VALUES (?, ?, ?)", rw_name, rune_id_1,
                           1)

            if rune_id_2 is not None:
                db.execute("INSERT INTO runeword_runes (name, rune_id, position) VALUES (?, ?, ?)", rw_name, rune_id_2,
                           2)

            if rune_id_3 is not None:
                db.execute("INSERT INTO runeword_runes (name, rune_id, position) VALUES (?, ?, ?)", rw_name, rune_id_3,
                           3)

            if rune_id_4 is not None:
                db.execute("INSERT INTO runeword_runes (name, rune_id, position) VALUES (?, ?, ?)", rw_name, rune_id_4,
                           4)

            if rune_id_5 is not None:
                db.execute("INSERT INTO runeword_runes (name, rune_id, position) VALUES (?, ?, ?)", rw_name, rune_id_5,
                           5)

            if rune_id_6 is not None:
                db.execute("INSERT INTO runeword_runes (name, rune_id, position) VALUES (?, ?, ?)", rw_name, rune_id_6,
                           6)

        return render_template("create_runewords.html", item_types=item_types, runes=runes, runewords=runewords)
    else:
        return render_template("create_runewords.html", item_types=item_types, runes=runes, runewords=runewords)


@app.route("/delete_runewords", methods=["GET", "POST"])
def delete_runewords():
    runewords = db.execute("SELECT name FROM runewords;")

    if request.method == "POST":
        name = str(request.form.get("name"))
        runeword = request.form.get("runeword")
        runeword_list = request.form.get("runeword_list")

        if runeword_list == "1":
            db.execute("DELETE FROM runeword_runes WHERE name = ?", name)

        if runeword == "1":
            db.execute("DELETE FROM runewords WHERE name = ?", name)

        return render_template("deleted_runewords.html", runewords=runewords)

    else:
        runewords = db.execute("SELECT name FROM runewords;")
        return render_template("delete_runewords.html", runewords=runewords)


if __name__ == '__main__':
    app.run()
