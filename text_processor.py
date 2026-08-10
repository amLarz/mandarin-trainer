import spacy

# load the English language model
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp(text)
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.lemma_)
        
    return doc
