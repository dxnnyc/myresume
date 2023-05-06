from flask import Flask
<<<<<<< HEAD
app = (__name__)
=======
app = Flask(__name__)
>>>>>>> cf14ab6ddc8743bd5fefd317de03d56f67c60e21

@app.route('/')
def hello_world():
    return 'Hello, World!'
