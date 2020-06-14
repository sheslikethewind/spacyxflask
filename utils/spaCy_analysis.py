#! /usr/bin/env python
import spacy
from .maitron import get_maitron_article

ID = 16519 # Bertin Emilienne on Maitron, full access with no user account

nlp = spacy.load('fr_core_news_sm')

def spaCy_analysis(string_to_analyse: str, article_getter=get_maitron_article) -> set:
    maitron = article_getter(id=ID)
    treat = nlp(maitron.get('article_intro') + maitron.get('article_content'))
    return set([t.text for t in treat.ents if t.label_ == 'LOC'])
