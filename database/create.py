import sqlite3
from sqlite3 import Error
from Models.Player import Player

import settings

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def init_db(db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS players
               (Id TEXT UNIQUE,
                Name TEXT,
                Mention TEXT,
               Games INTEGER,
               Wins INTEGER, 
               Losses INTEGER,
               Elo real)''')
    conn.commit()
    conn.close()

def update_player(id, name, mention, games, wins, losses, elo):
    conn = sqlite3.connect(settings.DB_DIR)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO players VALUES (?, ?, ?, ?, ?, ?, ?)", (id, name, mention, games, wins, losses, elo,))
    conn.commit()
    conn.close()

def get_player(id):
    conn = sqlite3.connect(settings.DB_DIR)
    cur = conn.cursor()
    cur.execute("SELECT * FROM players WHERE Id=?", (id,))
    player = cur.fetchone()
    conn.close()
    if(player == None):
        return None
    return Player(player[0], player[1], player[2], player[3], player[4], player[5], player[6])
