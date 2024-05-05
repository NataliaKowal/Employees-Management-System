from flask import Flask, jsonify, request
from flask_cors import CORS
from DatabaseInterface.Degree import *
from DatabaseInterface.Department import *
from DatabaseInterface.Employee import *

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
    
@app.route("/get_all_departments")
def server_get_all_departemnts():
    return get_all_departments("./DB/Employees.db")
    
@app.route("/add_department", methods=['POST'])
def server_add_department():
    data = request.json
    Name = data.get('Name')
    if Name != None:
        add_department("./DB/Employees.db", Name)
        return jsonify({'message': 'Dodano nowy rekord'}), 200
    else:
        return jsonify({'error': 'Nie dodano nowego rekorku'}), 400

@app.route("/delete_department", methods=['POST'])
def server_delete_department():
    data = request.json
    Id = data.get('Id')
    if Id != None:
        delete_degree("./DB/Employees.db", Id)
        return jsonify({'message': 'Usunieto rekord'}), 200
    else:
        return jsonify({'error': 'Nie Usunieto rekorku'}), 400
    
@app.route("/edit_department", methods=['POST'])
def server_edit_department():
    data = request.json
    Id = data.get('Id')
    Name = data.get('Name')
    if Id != None and Name != None:
        edit_department("./DB/Employees.db", Name, Id)  # Załóżmy, że ta funkcja istnieje
        return jsonify({'message': 'Edytowano rekord'}), 200
    else:
        return jsonify({'error': 'Nie edytowano rekorku'}), 400
    
@app.route("/get_all_employees")
def server_get_all_employees():
    return get_all_employees("./DB/Employees.db")
    
@app.route("/add_employee", methods=['POST'])
def server_add_employee():
    data = request.json
    Name = data.get('Name')
    Surname = data.get('Surname')
    PESEL_number = data.get('PESEL_number')
    Degree_Id = data.get('Degree_Id')
    Departemnt_Id = data.get('Departemnt_Id')
    Room_number = data.get('Room_number')
    Salary = data.get('Salary')
    if Name != None and Surname != None and PESEL_number != None and Degree_Id != None and Departemnt_Id != None and Room_number != None and Salary != None:
        add_employee("./DB/Employees.db", Name, Surname, PESEL_number, Degree_Id, Departemnt_Id, Room_number, Salary)
        return jsonify({'message': 'Dodano nowy rekord'}), 200
    else:
        return jsonify({'error': 'Nie dodano nowego rekordu'}), 400

@app.route("/delete_employee", methods=['POST'])
def server_delete_employee():
    data = request.json
    Id = data.get('Id')
    if Id != None:
        delete_employee("./DB/Employees.db", Id)
        return jsonify({'message': 'Usunieto rekord'}), 200
    else:
        return jsonify({'error': 'Nie Usunieto rekorku'}), 400
    
@app.route("/edit_employee", methods=['POST'])
def server_edit_employee():
    data = request.json
    Id = data.get('Id')
    Name = data.get('Name')
    Surname = data.get('Surname')
    PESEL_number = data.get('PESEL_number')
    Degree_Id = data.get('Degree_Id')
    Departemnt_Id = data.get('Departemnt_Id')
    Room_number = data.get('Room_number')
    Salary = data.get('Salary')
    if  Name != None and Surname != None and PESEL_number != None and Degree_Id != None and Departemnt_Id != None and Room_number != None and Salary != None:
        edit_employee("./DB/Employees.db", Id, Name,Surname, PESEL_number, Degree_Id, Departemnt_Id, Room_number, Salary)  # Załóżmy, że ta funkcja istnieje
        return jsonify({'message': 'Edytowano rekord'}), 200
    else:
        return jsonify({'error': 'Nie edytowano rekorku'}), 400 
    
if __name__ == '__main__':
    # Zmiana portu na 12345
    app.run(host="0.0.0.0", port=1234)
