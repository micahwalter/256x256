import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def twofiftysix():
    return 'Hello World!'

@app.route('/random')
def random():
	execfile('bin/random256.py')
	return 'hello random'