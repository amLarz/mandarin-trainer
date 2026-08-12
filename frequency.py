import sqlite3

con = sqlite3.connect('word_frequency.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS word_frequency (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL UNIQUE,
    frequency INTEGER DEFAULT 0
)
''')

con.commit()