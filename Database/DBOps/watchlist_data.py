import sqlite3
from pathlib import Path

# Database path
DB_PATH = Path("kubera.sqlite")

def insert_watchlist_data(data):
    missing = [k for k in ['stockID', 'currPrice', 'currTarget', 'currStopLoss', 'suggestedVolume', 'confidence'] if k not in data]
    if missing:
        print("Missing keys:", missing)
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO watchlist_data (stockID, currPrice, currTarget, currStopLoss, suggestedVolume, confidence)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (data['stockID'], data['currPrice'], data['currTarget'], data['currStopLoss'], data['suggestedVolume'], data['confidence']))
        conn.commit()
        print("Watchlist data inserted.")
        return True
    except sqlite3.IntegrityError as e:
        print("Error:", e)
    finally:
        conn.close()

def get_all_watchlist_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM watchlist_data")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_watchlist_data_entry(entry_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM watchlist_data WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    print(f"Entry with ID {entry_id} deleted from watchlist_data.")
