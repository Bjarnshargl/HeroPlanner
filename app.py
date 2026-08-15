from cs50 import SQL
from flask import Flask, redirect, render_template

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///instance/hero.db")


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
                                 i.item_class,
                                 i.runeword_id,
                                 i.ethereal,
                                 i.url,
                                 i.comment
                          FROM items i
                                   JOIN item_types it ON it.id = i.type
                          ORDER BY i.type, i.name""")
    return render_template("show_items.html", items=items)


@app.route("/create_items")
def create_items():
    return render_template("create_items.html")


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


if __name__ == '__main__':
    app.run()
