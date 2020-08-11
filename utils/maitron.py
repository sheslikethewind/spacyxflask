#! /usr/bin/env python
import requests
from bs4 import BeautifulSoup
from .constants import MAITRON_BASE_URL

def get_maitron_article(id: int) -> dict:
    maitron_getter = requests.get(MAITRON_BASE_URL + str(id))
    maitron_response = maitron_getter.text
    soup = BeautifulSoup(maitron_response, 'html.parser')
    article_title = soup.find("h1", "notice-titre")
    article_intro = soup.find("div", "intro")
    article_content = soup.find("div", "notice-texte entry")

    result = {
        'article_title': article_title.get_text(),
        'article_intro': article_intro.get_text(),
        'article_content': article_content.get_text(),
    }

    return result
