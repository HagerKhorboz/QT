import sqlite3

def init_db():
    conn = sqlite3.connect("players.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_player(name, age):
    conn = sqlite3.connect("players.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO players (name, age) VALUES (?, ?)",
        (name, age)
    )

    conn.commit()
    conn.close()


def get_player():
    conn = sqlite3.connect("players.db")
    cur = conn.cursor()

    cur.execute("SELECT id, name, age FROM players")
    rows = cur.fetchall()

    conn.close()
    return rows


def delete_player(player_id):
    conn = sqlite3.connect("players.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM players WHERE id = ?", (player_id,))

    conn.commit()
    conn.close()

def search_player(name):
    conn = sqlite3.connect("players.db")
    cur = conn.cursor()

    cur.execute("SELECT id, name, age FROM players WHERE name LIKE ?", (f"%{name}%",))
    rows = cur.fetchall()

    conn.close()
    return rows

