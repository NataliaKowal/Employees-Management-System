from flask import Flask

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route("/hello_world")
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1234)