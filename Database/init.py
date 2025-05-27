import sqlite3
from pathlib import Path

# Database path
DB_PATH = Path("Database/kubera.db")


def create_watchlist_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS watchlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL UNIQUE,
        name TEXT,
        exchange TEXT CHECK(exchange IN ('NSE', 'BSE')) DEFAULT 'NSE',
        added_on DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()

def create_watchlist_data_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS watchlist_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stockID INTEGER NOT NULL,
        currPrice DECIMAL,
        currTarget DECIMAL,
        currStopLoss DECIMAL,
        suggestedVolume INTEGER,
        confidence REAL,
        FOREIGN KEY(stockID) REFERENCES watchlist(id)
    );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Initiating a new thing...")