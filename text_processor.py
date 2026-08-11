import spacy
import csv

# load the English NLP model
nlp = spacy.load("en_core_web_sm")

def load_core_functional_words():
    CORE_FUNCTIONAL_WORDS = set()
    with open('core-functional-words-v1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            word = row[0]
            CORE_FUNCTIONAL_WORDS.add(word)
            
    return CORE_FUNCTIONAL_WORDS

    