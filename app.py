from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///instance/hero.db")

# Test

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/hero')
def hero():  # put application's code here
    return render_template("hero.html")


@app.route("/show_runes")
def show_runes():
    return render_template("show_runes.html")


@app.route("/show_items")
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
            """,name, item_type, item_class, runeword_name, ethereal, url, comment
        )

        return render_template("create_items.html", item_types=item_types, item_classes=item_classes,
                               runewords=runewords)

    else:
        return render_template("create_items.html", item_types=item_types, item_classes=item_classes,
                               runewords=runewords)


@app.route("/delete_items")
def delete_items():
    return render_template("delete_items.html")


@app.route("/show_merc")
def show_merc():
    return render_template("show_merc.html")


@app.route("/create_merc")
def create_merc():
    return render_template("create_merc.html")


@app.route("/delete_merc")
def delete_merc():
    return render_template("delete_merc.html")


@app.route("/show_hero")
def show_hero():
    return render_template("show_hero.html")


@app.route("/create_hero")
def create_hero():
    return render_template("create_hero.html")


@app.route("/delete_hero")
def delete_hero():
    return render_template("delete_hero.html")


@app.route("/show_runewords")
def show_runewords():
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
    return render_template("show_runewords.html", runewords=runewords)


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

        return render_template("delete_runewords.html", runewords=runewords)

    else:
        runewords = db.execute("SELECT name FROM runewords;")
        return render_template("delete_runewords.html", runewords=runewords)


if __name__ == '__main__':
    app.run()
