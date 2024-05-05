from flask import Flask, jsonify, request
from flask_cors import CORS
from DatabaseInterface.Degree import *

app = Flask(__name__, static_folder='.', template_folder='.')

CORS(app)

@app.route("/hello_world")
def hello_world():
    return jsonify(message="Ziemniaczki z koperkiem!")


@app.route("/get_all_degrees")
def server_get_all_degrees():
    return get_all_degrees("./DB/Employees.db")


@app.route("/add_degree", methods=['POST'])
def server_add_degree():
    data = request.json
    Name = data.get('Name')
    if Name != None:
        add_degree("./DB/Employees.db", Name)
        return jsonify({'message': 'Dodano nowy rekord'}), 200
    else:
        return jsonify({'error': 'Nie dodano nowego rekorku'}), 400

@app.route("/edit_degree", methods=['POST'])
def server_edit_degree():
    data = request.json
    Id = data.get('Id')
    Name = data.get('Name')
    if Id != None and Name != None:
        edit_degree("./DB/Employees.db", Name, Id)
        return jsonify({'message': 'Edytowano rekord'}), 200
    else:
        return jsonify({'error': 'Nie edytowano rekorku'}), 400
    
@app.route("/delete_degree", methods=['POST'])
def server_delete_degree():
    data = request.json
    Id = data.get('Id')
    if Id != None:
        delete_degree("./DB/Employees.db", Id)
        return jsonify({'message': 'Usunięto rekord'}), 200
    else:
        return jsonify({'error': 'Nie usunięto rekorku'}), 400

if __name__ == '__main__':
    # Zmiana portu na 12345
    app.run(host="0.0.0.0", port=1234)
