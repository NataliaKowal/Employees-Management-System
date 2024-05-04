import sqlite3

class Department:
    def __init__(self):
        self.Id = 0 
        self.Name = "Name"
    
    def __init__(self, new_Id, new_Name):
        self.Id = new_Id 
        self.Name = new_Name
    
    def __init__(self, tuple):
        self.Id = tuple[0] 
        self.Name = tuple[1]

    def __str__(self):
        return f"Id: {self.Id}, Name: {self.Name}"


def list_department (DB_path):
    """
    Opis: 
        Funkcja list_department służy do wyświetlania listy wszystkich działów zapisanych w bazie danych. \n
        Dla każdego działu wyświetlane są wszystkie dostępne informacje. \n
        Jest to przydatne do przeglądania zawartości tabeli Department i sprawdzania, jakie działy są obecnie zarejestrowane w systemie.
    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.

    """
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            records = cur.execute("SELECT * FROM Department").fetchall()
            departments = []
            for record in records:
                department = Department(record)
                print(department)
                departments.append(department)
                
    except sqlite3.Error as e: 
        print(f"error: {e}")


def add_department (DB_path, name):
    """
    Opis: 
        Funkcja add_department służy do dodawania nowego działu do bazy danych. \n
        Operacja ta polega na wstawieniu nowego rekordu do tabeli Department, zawierającego nazwę nowo dodanego działu. \n
        Jest to przydatne do rozszerzania struktury organizacyjnej firmy poprzez dodawanie nowych działów.
    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    - name (str): Nazwa nowo dodawanego działu.
    """
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Department (Name) VALUES (?)", (name, ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")


def edit_department (DB_path, name, Id):
    """
    Opis: 
        Funkcja edit_department służy do aktualizowania nazwy istniejącego działu w bazie danych na podstawie podanego unikalnego identyfikatora (Id).\n
        Pozwala na zmianę nazwy działu, co jest przydatne w przypadku reorganizacji lub błędów w nazewnictwie.

        
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    - Id (int): Unikalny identyfikator działu, który ma zostać usunięty z bazy danych.
    """
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("UPDATE Department SET Name = ? WHERE Id = ?", (name, Id,  ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")

def delete_department (DB_path, Id):
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Department WHERE Id = ?", (Id, ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")