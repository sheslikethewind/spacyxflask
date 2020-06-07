#! /usr/bin/env python
from flask import Flask, render_template, request
from spaCy_analysis import spaCy_analysis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response():
    try:
        if request.method == 'POST':
            form_input = request.form.get('search')
            response = spaCy_analysis(string_to_analyse=form_input)
            return render_template('index.html', spaCyResponse=response)
        else:
            return render_template('index.html', spaCyResponse="Error: Please try again")
    except:
        return render_template('index.html', spaCyResponse="Error: Please try again")


if __name__ == '__main__':
    app.run(debug=True)