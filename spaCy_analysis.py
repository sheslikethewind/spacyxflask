import spacy

nlp = spacy.load('en_core_web_sm')

def spaCy_analysis(string_to_analyse: str):
    doc = nlp(string_to_analyse)
    return [(w.text, w.pos_) for w in doc]