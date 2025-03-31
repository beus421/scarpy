from flask import Flask, render_template, jsonify
import json
import os
import random

app = Flask(__name__)

# Load the quotes data
def load_quotes():
    with open('../quotes.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quotes')
def get_quotes():
    quotes = load_quotes()
    return jsonify(quotes)

@app.route('/api/random-quote')
def get_random_quote():
    quotes = load_quotes()
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)