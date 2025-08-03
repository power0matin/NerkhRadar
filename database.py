import sqlite3
from contextlib import contextmanager


@contextmanager
def get_db():
    conn = sqlite3.connect("bot.db")
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    with get_db() as conn:
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                currency TEXT DEFAULT 'toman',
                report_time TEXT DEFAULT '14:00',
                crypto_list TEXT DEFAULT 'btc,eth,sol'
            )
        """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS alerts (
                user_id INTEGER,
                asset TEXT,
                condition TEXT,
                value REAL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """
        )
        conn.commit()


def add_alert(user_id, asset, condition, value):
    with get_db() as conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO alerts (user_id, asset, condition, value) VALUES (?, ?, ?, ?)",
            (user_id, asset, condition, value),
        )
        conn.commit()


def get_user_alerts(user_id):
    with get_db() as conn:
        c = conn.cursor()
        c.execute(
            "SELECT asset, condition, value FROM alerts WHERE user_id = ?", (user_id,)
        )
        return [
            {"asset": row[0], "condition": row[1], "value": row[2]}
            for row in c.fetchall()
        ]


def update_user_settings(user_id, **kwargs):
    with get_db() as conn:
        c = conn.cursor()
        for key, value in kwargs.items():
            c.execute(
                f"INSERT OR REPLACE INTO users (id, {key}) VALUES (?, ?)",
                (user_id, value),
            )
        conn.commit()


def get_user_settings(user_id):
    with get_db() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = c.fetchone()
        return dict(result) if result else {}


def get_all_users():
    with get_db() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        return [dict(row) for row in c.fetchall()]
