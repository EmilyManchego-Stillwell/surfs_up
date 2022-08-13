from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/v1.0/friendly_greeting')
def friendly_greeting():
    return 'I hope you are having a wonderful day!'