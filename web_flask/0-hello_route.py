#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/airbnb-onepage/', strict_slashes=False)
def index():
    """Returns the content of the /airbnb-onepage/ route."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=False)
    gunicorn app:app --bind 0.0.0.0:8000
