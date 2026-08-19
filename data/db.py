import sqlite3

con = sqlite3.connect('mandarin.db')
cur = con.cursor()

# WORDS TABLE
cur.execute('''CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY,
    word TEXT NOT NULL UNIQUE,
    frequency INTEGER NOT NULL DEFAULT 0
)''')

# SENTENCES TABLE
cur.execute('''CREATE TABLE IF NOT EXISTS sentences (
    id INTEGER PRIMARY KEY,
    sentence TEXT NOT NULL
)''')

# WORDS_SENTENCES_LINKS TABLE
cur.execute('''CREATE TABLE IF NOT EXISTS words_sentences_links (
    word_id INTEGER NOT NULL,
    sentence_id INTEGER NOT NULL,
    FOREIGN KEY (word_id) REFERENCES words(id),
    FOREIGN KEY (sentence_id) REFERENCES sentences(id)
    PRIMARY KEY (word_id, sentence_id)
)''')

con.commit()

def insert_word(word):
    cur.execute("INSERT OR IGNORE INTO words (word) VALUES (?)", 
                (word,)
    )
        
    cur.execute("UPDATE words SET frequency = frequency + 1 WHERE word = ?", 
                (word,)
    )
    
    word_id = cur.execute("SELECT id FROM words WHERE word = ?",
                          (word,)
            ).fetchone()[0]
    
    con.commit()
    
    return word_id

def insert_sentence(sentence):
    cur.execute("INSERT INTO sentences (sentence) VALUES (?)", 
                (sentence,)
    )
    
    sentence_id = cur.lastrowid
    
    con.commit()
    
    return sentence_id

def word_sentence_link(word_id, sentence_id):
    cur.execute("INSERT OR IGNORE INTO words_sentences_links (word_id, sentence_id) VALUES (?, ?)",
                (word_id, sentence_id)
    )
    con.commit()
    
    return

def save_to_database(results):
    for record in results:
        sentence_id = insert_sentence(record["text"])
        for lemma in record["classification"]["tier1_content"]:
            word_id = insert_word(lemma)
            word_sentence_link(word_id, sentence_id)
    
    con.commit()
    
    return