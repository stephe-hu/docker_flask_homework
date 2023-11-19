from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    math = 5 + 5
    return f'Hello, World! From a Flask app in a Docker container! Math = {math}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')