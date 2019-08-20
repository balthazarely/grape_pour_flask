from flask import Flask, g

import models

DEBUG = True
PORT = 8000

app = Flask(__name__)
# this is initializing an instance of the Flask class.

@app.before_request
def before_request():
    """ Connect to the database before each request"""
    g.db = models.database
    g.db.connect()

@app.after_request
def after_request(response):
    """ Close database after each request """
    return response

@app.route('/')
def index():
    return 'hi'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)