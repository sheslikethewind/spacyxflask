#! /usr/bin/env python
from flask import Flask, render_template, request
from utils.spaCy_analysis import spaCy_analysis
from utils.coordonates import get_nominatim_coordonates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response():
    try:
        if request.method == 'POST':
            form_input = request.form.get('search')
            cities = spaCy_analysis(string_to_analyse=form_input)
            coordonates = get_nominatim_coordonates(entities=cities)
            return render_template('index.html', coordonates=coordonates, cities=str(len(cities)) + ' places found.')
        else:
            return render_template('index.html', spaCyResponse="Error: Please try again")
    except:
        return render_template('index.html', spaCyResponse="Error: Please try again")


if __name__ == '__main__':
    app.run(debug=True)