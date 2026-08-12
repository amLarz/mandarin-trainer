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

def classify_words(token):
    lemma = token.lemma_.lower()
    CORE_FUNCTIONAL_WORDS = load_core_functional_words()
    
    # classify words in the text from the tiers
    if lemma in CORE_FUNCTIONAL_WORDS:
        return "tier0_function"
    if token.pos_ in ["NOUN", "VERB", "ADJ"]:
        return "tier1_content"
    return None
    
def process_text(text):
    # process the text using spaCy
    doc = nlp(text)
    tiers = {"tier0_function": [], "tier1_content": []}
    for token in doc:
        classification = classify_words(token)
        if classification:
            tiers[classification].append(token.lemma_.lower())
        
    return tiers

