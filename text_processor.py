import spacy
from transcribe import result

nlp = spacy.load("en_core_web_sm")
doc = nlp(result["text"])

for token in doc:
    print(token.text, token.pos_, token.dep_, token.lemma_)
