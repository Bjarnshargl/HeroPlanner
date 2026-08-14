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

if __name__ == '__main__':
    app.run()
