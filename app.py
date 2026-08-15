from cs50 import SQL
from flask import Flask, render_template

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///heroes.db")

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
    return render_template("show_items.html")

@app.route("/create_items")
def create_items():
    return render_template("create_items.html")

@app.route("/delete_items")
def delete_items():
    return render_template("delete_items.html")

if __name__ == '__main__':
    app.run()
