import sqlite3
import os
from source.utils import fib_mod_sequence,digital_root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB_PATH = os.path.join(BASE_DIR, "data", "hmm_data.db")

def init_and_populate_db(db_path=None):
    path = db_path or DEFAULT_DB_PATH
    conn = sqlite3.connect(path)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS fib (
                 n INTEGER PRIMARY KEY, value INTEGER)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS ker_diff (
                 x INTEGER, y INTEGER, diff INTEGER, ker INTEGER,
                 PRIMARY KEY (x, y))''')
    
    # Заполнение 1D
    fibs = fib_mod_sequence(1500, 100)
    for i, v in enumerate(fibs):
        c.execute("INSERT OR IGNORE INTO fib VALUES (?, ?)", (i, v))
    
    # Заполнение 2D (50x50 = 2500 записей)
    for x in range(1, 51):
        for y in range(1, 51):
            diff = abs(x*x - y*y)
            ker = digital_root(diff)
            c.execute("INSERT OR IGNORE INTO ker_diff VALUES (?,?,?,?)", 
                     (x, y, diff, ker))
    
    conn.commit()
    conn.close()