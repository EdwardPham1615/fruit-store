#!/usr/bin/env python

from flask import Flask
from domain.routes import fruit_store

app = Flask(__name__)
app.register_blueprint(fruit_store)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
