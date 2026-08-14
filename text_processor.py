import token

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

# recursive function to filter out stop words and return the lemmas of the remaining words
def filter_words_layer1(doc, index=0):
    
    if index >= len(doc): # if the index is reached end the function
        return []
    
    # initializing variables for the current token
    token = doc[index]
    lemma = token.lemma_
    
    if not token.is_stop:
        return [lemma] + filter_words_layer1(doc, index + 1)
    
    return filter_words_layer1(doc, index + 1)


def filter_words_layer2(doc, layer1_result, index=0):
    
    # orphan dependencies that are not useful for our purposes
    ORPHAN_DEPS = {
    "punct",
    "det",
    "expl",
    "discourse",
    "intj",
    }
    
    if index >= len(layer1_result): # if the index is reached end the function
        return [] 
    
    # initializing variables for the current token
    token = doc[index]
    lemma = token.lemma_
    dep = token.dep_
    
    if dep in ORPHAN_DEPS:
        return filter_words_layer2(doc, layer1_result, index + 1)
    
    return [lemma] + filter_words_layer2(doc, layer1_result, index + 1)

def filter_words(doc):
    layer1_result = filter_words_layer1(doc)
    layer2_result = filter_words_layer2(doc, layer1_result)
    return layer1_result, layer2_result

def process_text(text):
    # process the text using spaCy
    doc = nlp(text)
    
    return filter_words(doc)
        