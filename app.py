from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Hello, ARM docker world"

@app.route('/v2')

def home_v2():
    return "Hello v2, Arm world"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
