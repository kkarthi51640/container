from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

app.run(host='15.207.111.162', port=5000)
