from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from DatabaseInterface.Degree import *
from DatabaseInterface.Department import *
from DatabaseInterface.Employee import *

app = Flask(__name__, static_folder='.', template_folder='.')

CORS(app)

DB_PATH = "./DB/Employees.db"

EMPLOYEE_FIELDS = ['Name', 'Surname', 'PESEL_number', 'Degree_Id', 'Departemnt_Id', 'Room_number', 'Salary']


def get_fields(names):
    """Zwraca listę wartości z JSON-a żądania albo None, jeśli brakuje któregoś pola."""
    data = request.get_json(silent=True) or {}
    values = [data.get(name) for name in names]
    if any(value is None for value in values):
        return None
    return values


def list_response(json_str):
    """Odpowiedź dla endpointów get_all_*: 500, jeśli odczyt z bazy się nie udał."""
    if json_str is None:
        return jsonify({'error': 'Błąd odczytu z bazy danych'}), 500
    return Response(json_str, mimetype='application/json')


def result_response(success, ok_message):
    """Odpowiedź dla add/edit/delete: 200 przy sukcesie, 500 przy błędzie bazy."""
    if success:
        return jsonify({'message': ok_message}), 200
    return jsonify({'error': 'Błąd bazy danych'}), 500


def missing_fields_response():
    return jsonify({'error': 'Brak wymaganych pól w żądaniu'}), 400


@app.route("/hello_world")
def hello_world():
    return jsonify(message="Ziemniaczki z koperkiem!")


# ---------- Degrees ----------

@app.route("/get_all_degrees")
def server_get_all_degrees():
    return list_response(get_all_degrees(DB_PATH))


@app.route("/add_degree", methods=['POST'])
def server_add_degree():
    fields = get_fields(['Name'])
    if fields is None:
        return missing_fields_response()
    return result_response(add_degree(DB_PATH, *fields), 'Dodano nowy rekord')


@app.route("/edit_degree", methods=['POST'])
def server_edit_degree():
    fields = get_fields(['Id', 'Name'])
    if fields is None:
        return missing_fields_response()
    Id, Name = fields
    return result_response(edit_degree(DB_PATH, Name, Id), 'Edytowano rekord')


@app.route("/delete_degree", methods=['POST'])
def server_delete_degree():
    fields = get_fields(['Id'])
    if fields is None:
        return missing_fields_response()
    return result_response(delete_degree(DB_PATH, *fields), 'Usunięto rekord')


# ---------- Departments ----------

@app.route("/get_all_departments")
def server_get_all_departments():
    return list_response(get_all_departments(DB_PATH))


@app.route("/add_department", methods=['POST'])
def server_add_department():
    fields = get_fields(['Name'])
    if fields is None:
        return missing_fields_response()
    return result_response(add_department(DB_PATH, *fields), 'Dodano nowy rekord')


@app.route("/edit_department", methods=['POST'])
def server_edit_department():
    fields = get_fields(['Id', 'Name'])
    if fields is None:
        return missing_fields_response()
    Id, Name = fields
    return result_response(edit_department(DB_PATH, Name, Id), 'Edytowano rekord')


@app.route("/delete_department", methods=['POST'])
def server_delete_department():
    fields = get_fields(['Id'])
    if fields is None:
        return missing_fields_response()
    # Wcześniej wywoływało się tu delete_degree, co kasowało stopień naukowy zamiast działu.
    return result_response(delete_department(DB_PATH, *fields), 'Usunięto rekord')


# ---------- Employees ----------

@app.route("/get_all_employees")
def server_get_all_employees():
    return list_response(get_all_employees(DB_PATH))


@app.route("/add_employee", methods=['POST'])
def server_add_employee():
    fields = get_fields(EMPLOYEE_FIELDS)
    if fields is None:
        return missing_fields_response()
    return result_response(add_employee(DB_PATH, *fields), 'Dodano nowy rekord')


@app.route("/edit_employee", methods=['POST'])
def server_edit_employee():
    fields = get_fields(['Id'] + EMPLOYEE_FIELDS)
    if fields is None:
        return missing_fields_response()
    return result_response(edit_employee(DB_PATH, *fields), 'Edytowano rekord')


@app.route("/delete_employee", methods=['POST'])
def server_delete_employee():
    fields = get_fields(['Id'])
    if fields is None:
        return missing_fields_response()
    return result_response(delete_employee(DB_PATH, *fields), 'Usunięto rekord')


if __name__ == '__main__':
    # Frontend łączy się z http://localhost:1234
    app.run(host="0.0.0.0", port=1234)
