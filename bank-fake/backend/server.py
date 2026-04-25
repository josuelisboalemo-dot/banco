from flask import Flask, request, jsonify, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret"

def db():
    return sqlite3.connect("bank.db")

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                (data["username"], data["password"]))

    user = cur.fetchone()

    if user:
        return jsonify({"ok": True})

    return jsonify({"ok": False})