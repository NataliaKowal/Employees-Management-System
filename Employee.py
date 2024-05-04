import sqlite3

class Employee:
    def __init__(self):
        self.Id = 0 
        self.Name = "Name"
        self.Surname = "Surname"
        self.PESEL_number = 0
        self.Degree_Id = -1
        self.Departemnt_Id = -1
        self.Room_number = -1
        self.Salary = 0.0
    
    def __init__(self, new_Id, new_Name, new_Surname, new_PESEL_number, new_Degree_Id, new_Departemnt_Id, new_Room_number, new_Salary):
        self.Id = new_Id 
        self.Name = new_Name
        self.Surname = new_Surname
        self.PESEL_number = new_PESEL_number
        self.Degree_Id = new_Degree_Id
        self.Departemnt_Id = new_Departemnt_Id
        self.Room_number = new_Room_number
        self.Salary = new_Salary
    
def list_employees (DB_path):
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            records = cur.execute("SELECT * FROM Employees").fetchall()
            employees = []
            print("Employees in database:")
            for record in records:
                employee = Employee(record)
                print(f" - {employee}")
                employees.append(employee)
                
    except sqlite3.Error as e: 
        print(f"error: {e}")


def add_employee (DB_path, Name, Surname, PESEL_number, Degree_Id, Departemnt_Id, Room_number, Salary):
    """
    Opis: Fucnkj.......
    
    Autor: Imię i nazwisko autora
    
    Argumenty:
    DB_path (str): Opis argumentu arg1.
    Name (str): Opis argumentu arg2.
    """
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            querry = """
                INSERT INTO Employees (Name, Surname, PESEL_number, Degree_Id, Departemnt_Id, Room_number, Salary) 
                VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(querry, (Name, Surname, PESEL_number, Degree_Id, Departemnt_Id, Room_number, Salary ))
            con.commit()
            print(f"Added new employee to database with data: Name: {Name}, Surname: {Surname}, PESEL_number: {PESEL_number}, Degree_Id: {Degree_Id}, Departemnt_Id: {Departemnt_Id}, Room_number: {Room_number}, Salary: {Salary}")
    except sqlite3.Error as e: 
        print(f"error: {e}")

def edit_employee (DB_path, Id, Name, Surname, PESEL_number, Degree_Id, Departemnt_Id, Room_number, Salary):
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            querry = """
                UPDATE Employees 
                SET Name = ?, Surname = ?, PESEL_number = ?, Degree_Id = ?, Departemnt_Id = ?, Room_number = ?, Salary = ?  
                WHERE Id = ?"""
            cur.execute(querry, (Name, Surname, PESEL_number, Degree_Id, Departemnt_Id, Room_number, Salary, Id))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")

def delete_employee (DB_path, Id):
    try: 
        with sqlite3.connect(DB_path) as con:
            querry = "DELETE FROM Employees WHERE Id = ?"
            cur = con.cursor()
            cur.execute(querry, (Id, ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")