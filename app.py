#! /usr/bin/env python
from flask import Flask, render_template, request
from utils.maitron import get_maitron_article
from utils.constants import ARTICLE_ID

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response():
    try:
        if request.method == 'POST':
            article = get_maitron_article(id=ARTICLE_ID)
            return render_template('index.html', article=article)
        else:
            return render_template('index.html', article="Error: Please try again")
    except:
        return render_template('index.html', article="Error: Please try again")


if __name__ == '__main__':
    app.run(debug=True)
