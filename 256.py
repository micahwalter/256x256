import os
from flask import Flask
from bin import random256

app = Flask(__name__)

@app.route('/')
def twofiftysix():
    return '256x256'

@app.route('/random')
def random():
	return random256.randomImage()
