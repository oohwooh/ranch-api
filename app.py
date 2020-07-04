import random

from flask import Flask

import ranch

app = Flask(__name__)


@app.route('/brands')
def list_brands():
    """Returns a dict of ranch brands"""
    return ranch.brands


@app.route('/brands/random')
def random_brand():
    """Returns a random ranch brand"""
    return random.choice(list(ranch.brands.values()))
