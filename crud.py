import sqlite3

def get_users(db: sqlite3.Connection):
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email, phone, balance FROM users")
    rows = cursor.fetchall()
    return [{"id": r[0], "name": r[1], "email": r[2], "phone": r[3], "balance": r[4]} for r in rows]

def update_wallet(db: sqlite3.Connection, user_id: int, amount: float):
    cursor = db.cursor()
    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    row = cursor.fetchone()
    if not row:
        raise Exception("User not found")

    new_balance = row[0] + amount
    cursor.execute("UPDATE users SET balance=? WHERE id=?", (new_balance, user_id))
    cursor.execute("INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?)",
                   (user_id, amount, "credit" if amount > 0 else "debit"))
    db.commit()
    return new_balance

def get_transactions(db: sqlite3.Connection, user_id: int):
    cursor = db.cursor()
    cursor.execute("SELECT id, user_id, amount, type, timestamp FROM transactions WHERE user_id=?", (user_id,))
    rows = cursor.fetchall()
    return [{"id": r[0], "user_id": r[1], "amount": r[2], "type": r[3], "timestamp": r[4]} for r in rows]
