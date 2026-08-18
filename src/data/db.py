import sqlite3

con = sqlite3.connect('mandarin.db')
cur = con.cursor()

# WORDS TABLE
cur.execute('''CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    frequency INTEGER NOT NULL DEFAULT 0
)''')

# SENTENCES TABLE
cur.execute('''CREATE TABLE IF NOT EXISTS sentences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sentence TEXT NOT NULL
)''')

# WORDS_SENTENCES TABLE
cur.execute('''CREATE TABLE IF NOT EXISTS words_sentences (
    word_id INTEGER NOT NULL,
    sentence_id INTEGER NOT NULL,
    FOREIGN KEY (word_id) REFERENCES words(id),
    FOREIGN KEY (sentence_id) REFERENCES sentences(id)
)''')

con.commit()