#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/airbnb-onepage/', strict_slashes=False)
def index():
    """Returns the content of the /airbnb-onepage/ route."""
    return 'This is the Airbnb One Page application.'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
