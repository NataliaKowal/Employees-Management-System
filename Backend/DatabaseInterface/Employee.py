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
    """
    Opis: 
        Funkcja list_employees służy do wyświetlania listy wszystkich pracowników zapisanych w bazie danych. \n
        Dla każdego pracownika wyświetlane są wszystkie dostępne informacje. \n
        Funkcja ta jest przydatna do przeglądania zawartości tabeli Employees i sprawdzania, którzy pracownicy są obecnie zarejestrowani w systemie. 

    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    
    Zwraca:
    typ: Opis tego, co funkcja zwraca.
    """
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
    Opis: 
        Funkcja add_employee służy do dodawania nowego pracownika do bazy danych. \n
        Wykorzystuje do tego połączenie z bazą danych SQLite. \n
        Po pomyślnym dodaniu pracownika, funkcja wyświetla informacje o dodanym pracowniku.
    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    - Name (str): Imię nowego pracownika.
    - Surname (str): Nazwisko nowego pracownika.
    - PESEL_number (str): Numer PESEL nowego pracownika.
    - Degree_Id (int): Identyfikator stopnia naukowego nowego pracownika.
    - Departemnt_Id (int): Identyfikator działu, do którego zostanie przypisany nowy pracownik.
    - Room_number (int): Numer pokoju, który zostanie przypisany nowemu pracownikowi.
    - Salary (float): Wynagrodzenie nowego pracownika.
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
    """
    Opis: 
        Funkcja edit_employee służy do aktualizowania danych istniejącego pracownika w bazie danych. \n
        Umożliwia zmianę takich informacji jak imię, nazwisko, numer PESEL, identyfikator stopnia naukowego, identyfikator działu, numer pokoju oraz wynagrodzenie pracownika.\n
        W przypadku niepowodzenia operacji, funkcja wyświetla komunikat o błędzie.
    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    - Id (int): Unikalny identyfikator pracownika, którego dane mają być aktualizowane.
    - Name (str): Nowe imię pracownika.
    - Surname (str): Nowe nazwisko pracownika.
    - PESEL_number (str): Nowy numer PESEL pracownika.
    - Degree_Id (int): Nowy identyfikator stopnia naukowego pracownika.
    - Departemnt_Id (int): Nowy identyfikator działu, do którego przypisany jest pracownik.
    - Room_number (int): Nowy numer pokoju przypisany do pracownika.
    - Salary (float): Nowe wynagrodzenie pracownika.
    """
    # Tutaj umieść ciało funkcji
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
    """
    Opis: 
        Funkcja delete_employee służy do usuwania pracownika z bazy danych na podstawie podanego unikalnego identyfikatora (Id).\n
        Operacja ta usuwa wszystkie informacje związane z pracownikiem o określonym Id z tabeli Employees. \n
        W przypadku wystąpienia błędu podczas operacji usuwania, funkcja wyświetla komunikat o błędzie.
    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    - Id (int): Unikalny identyfikator pracownika, który ma zostać usunięty z bazy danych.
    """
    try: 
        with sqlite3.connect(DB_path) as con:
            querry = "DELETE FROM Employees WHERE Id = ?"
            cur = con.cursor()
            cur.execute(querry, (Id, ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")