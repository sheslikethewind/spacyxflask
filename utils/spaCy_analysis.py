#! /usr/bin/env python
import spacy
from .maitron import get_maitron_article
from .constants import ARTICLE_ID

nlp = spacy.load('fr_core_news_sm')

def spaCy_analysis(article_getter=get_maitron_article) -> list:
    maitron = article_getter(id=ARTICLE_ID)
    treat = nlp(maitron.get('article_intro') + maitron.get('article_content'))
    return list(set([t.text for t in treat.ents if t.label_ == 'LOC']))
