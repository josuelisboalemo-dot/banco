@app.route("/pix", methods=["POST"])
def pix():
    data = request.json

    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT balance FROM users WHERE username=?",
                (data["user"],))
    sender_balance = cur.fetchone()[0]

    if sender_balance < data["value"]:
        return jsonify({"error": "saldo insuficiente"})

    cur.execute("UPDATE users SET balance = balance - ? WHERE username=?",
                (data["value"], data["user"]))

    cur.execute("UPDATE users SET balance = balance + ? WHERE username=?",
                (data["value"], data["to"]))

    cur.execute("INSERT INTO transactions VALUES (NULL,?,?,?,?)",
                (data["user"], data["to"], data["value"], str(datetime.now())))

    conn.commit()
    return jsonify({"ok": True})