import spacy
import csv

# load the English NLP model
nlp = spacy.load("en_core_web_sm")

def load_core_functional_words():
    CORE_FUNCTIONAL_WORDS = set()
    with open('core-functional-words-v1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            word = row[0].lower()
            CORE_FUNCTIONAL_WORDS.add(word)
            
    return CORE_FUNCTIONAL_WORDS

CORE_FUNCTIONAL_WORDS = load_core_functional_words()

# TODO: recursive function, use token.text to print the doc[index] of your choice
def filter_words_layer1(doc, index=0):
    lemma = token.lemma_
    
    if index == len:
        return []
    
    if not lemma.is_stop:
        return [lemma ]
    
    return
def filter_words(doc):
    filter_words_layer1(doc)
    
    return None

def process_text(text):
    # process the text using spaCy
    doc = nlp(text)
    
    filter_words(doc)
        