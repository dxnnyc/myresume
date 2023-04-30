from flask import flask
app = (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'