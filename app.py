#! /usr/bin/env python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response():
    try:
        if request.method == 'POST':
            return render_template('index.html', response="Hello World")
        else:
            return render_template('index.html', response="Error: Please try again")
    except:
        return render_template('index.html', response="Error: Please try again")


if __name__ == '__main__':
    app.run(debug=True)
