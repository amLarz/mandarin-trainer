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

def update_word_frequency(word):
    cur.execute('SELECT frequency FROM word_frequency WHERE word = ?', (word,))
    result = cur.fetchone()
    
    if result is None:
        cur.execute('INSERT INTO word_frequency (word, frequency) VALUES (?, ?)', 
                    (word, 1)
        )
    else:
        cur.execute('UPDATE word_frequency SET frequency = frequency + 1 WHERE word = ?', 
                    (word,)
        )
    
    con.commit()
    
    cur.execute('SELECT * FROM word_frequency')
    result = cur.fetchall()
    print(result)
    
    return 0

# TODO: update the database with the processed tiers
def update_database(tiers):
    for tier in tiers.keys():
        print(tier)
        for word in tiers.values():
            print(word)

    return 0