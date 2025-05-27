import sqlite3
from pathlib import Path

# Database path
DB_PATH = Path("Database/kubera.db")

def insert_watchlist(data):
    
    missing = [k for k in [ 'symbol', 'name', 'exchange'] if k not in data]
    if missing: 
        print("Missing keys:", missing) 
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO watchlist (symbol, name, exchange)
        VALUES (?, ?, ?)
        """, (data['symbol'], data['name'], data['exchange']))
        conn.commit()
        print("Stock added to watchlist.")
        return True
    except sqlite3.IntegrityError as e:
        print("Error:", e)
    finally:
        conn.close()

def get_all_watchlist():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM watchlist")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_watchlist_entry(entry_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # First delete related entries in watchlist_data
    cursor.execute("DELETE FROM watchlist_data WHERE stockID = ?", (entry_id,))

    # Then delete from watchlist
    cursor.execute("DELETE FROM watchlist WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    print(f"Entry with ID {entry_id} and its related data deleted.")
