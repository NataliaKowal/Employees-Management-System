import sqlite3
import json

class Degree:
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


def get_all_degrees (DB_path):
    """
    Opis: 
        Funkcja list_degrees służy do wyświetlania listy wszystkich stopni naukowych zapisanych w bazie danych. \n
        Dla każdego stopnia wyświetlane są wszystkie dostępne informacje. \n
        Jest to przydatne do przeglądania zawartości tabeli Degree i sprawdzania, jakie stopnie naukowe są obecnie zarejestrowane w systemie.
    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.

    """
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            rows = cur.execute("SELECT * FROM Degree").fetchall()
            columns = [description[0] for description in cur.description]
            resoults = [dict(zip(columns, row)) for row in rows]
            json_str = json.dumps(resoults, indent=4)
            print(json_str)
            return json_str
    except sqlite3.Error as e: 
        print(f"error: {e}")


def add_degree (DB_path, name):
    """
    Opis:
        Funkcja add_degree służy do dodawania nowego stopnia naukowego do bazy danych.\n
        Operacja ta polega na wstawieniu nowego rekordu do tabeli Degree, zawierającego nazwę nowo dodanego stopnia naukowego.\n
        Jest to przydatne do rozszerzania listy dostępnych stopni naukowych w systemie edukacyjnym lub organizacyjnym.

    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    - name (str): Nazwa nowo dodawanego stopnia naukowego.

    """
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Degree (Name) VALUES (?)", (name, ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")


def edit_degree (DB_path, name, Id):
    """
    Opis: 
        Funkcja edit_degree służy do aktualizowania nazwy istniejącego stopnia naukowego w bazie danych na podstawie podanego unikalnego identyfikatora (Id).\n
        Umożliwia zmianę nazwy stopnia, co jest przydatne w przypadku korekt lub aktualizacji danych dotyczących stopni naukowych.

    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    - name (str): Nowa nazwa stopnia naukowego.
    - Id (int): Unikalny identyfikator stopnia naukowego, którego nazwa ma zostać zmieniona.

    """
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("UPDATE Degree SET Name = ? WHERE Id = ?", (name, Id,  ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")


def delete_degree (DB_path, Id):
    """
    Opis:
        Funkcja delete_degree służy do usuwania stopnia naukowego z bazy danych na podstawie podanego unikalnego identyfikatora (Id).\n
        Operacja ta usuwa wszystkie informacje związane ze stopniem naukowym o określonym Id z tabeli Degree.\n
        Jest to przydatne w przypadku likwidacji nieaktualnych lub błędnie wprowadzonych stopni naukowych.

    
    Autor: Natalia Kowal
    
    Argumenty:
    - DB_path (str): Ścieżka do bazy danych, z którą funkcja nawiązuje połączenie.
    - Id (int): Unikalny identyfikator stopnia naukowego, który ma zostać usunięty z bazy danych.
    
    """
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Degree WHERE Id = ?", (Id, ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")