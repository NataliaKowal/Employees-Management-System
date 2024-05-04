from flask import Flask, jsonify
from flask_cors import CORS
from DatabaseInterface.Degree import *

app = Flask(__name__, static_folder='.', template_folder='.')

CORS(app)

@app.route("/hello_world")
def hello_world():
    return jsonify(message="Ziemniaczki z koperkiem!")


@app.route("/get_all_degrees")
def get_all_degrees():
    return list_degrees()

if __name__ == '__main__':
    # Zmiana portu na 12345
    app.run(host="0.0.0.0", port=1234)
