import spacy
import csv

# load the English NLP model
nlp = spacy.load("en_core_web_sm")

# MIGHT REMOVE
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
def is_stop_filter(token):
    # if the token is a stop word, move on.
    if token.is_stop:
        return True

    return False

def is_orphaned_filter(token):
    
    # orphan dependencies that are not useful for our purposes
    ORPHAN_DEPS = {
    "punct",
    "det",
    "expl",
    "discourse",
    "intj",
    }
    
    dep = token.dep_
    
    # if there are any orphan dependencies, move on.
    if dep in ORPHAN_DEPS:
        return True

    return False

# TODO: UNFINISHED
def classify_words(token):
    lemma = token.lemma_
    dep = token.dep_
    
    if lemma in CORE_FUNCTIONAL_WORDS:
        return "tier0_functional"
    if token.pos_ in ["NOUN", "VERB", "ADJ", "ADV", "PROPN", "NUM"]:
        return "tier1_content"
    
    return None

def filter_words(doc):
    classification = {"tier0_functional": [], "tier1_content": []}
    for token in doc:
        # layer 1: filter out stop words
        is_stop = is_stop_filter(token)

        if is_stop == True:
            is_orphaned = True
        else:
            # layer 2: filter out orphan dependencies
            is_orphaned = is_orphaned_filter(token)

        if not is_stop and not is_orphaned:
            # layer 3: classify words
            classified_words = classify_words(token)
            
            if classified_words:
                classification[classified_words].append(token.lemma_)
            
    return classification

def process_text(text):
    # process the text using spaCy
    doc = nlp(text)
    
    return filter_words(doc)
        