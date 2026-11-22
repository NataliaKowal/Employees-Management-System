import sqlite3
import json

class Employee:
    def __init__(self, new_Id=0, new_Name="Name", new_Surname="Surname", new_PESEL_number=0,
                 new_Degree_Id=-1, new_Departemnt_Id=-1, new_Room_number=-1, new_Salary=0.0):
        self.Id = new_Id
        self.Name = new_Name
        self.Surname = new_Surname
        self.PESEL_number = new_PESEL_number
        self.Degree_Id = new_Degree_Id
        self.Departemnt_Id = new_Departemnt_Id
        self.Room_number = new_Room_number
        self.Salary = new_Salary

    @classmethod
    def from_tuple(cls, row):
        """Tworzy obiekt z wiersza bazy danych (kolejność kolumn jak w tabeli Employees)."""
        return cls(*row)

def get_all_employees (DB_path):
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
            rows = cur.execute("SELECT * FROM Employees").fetchall()
            columns = [description[0] for description in cur.description]
            resoults = [dict(zip(columns, row)) for row in rows]
            json_str = json.dumps(resoults, indent=4)
            print(json_str)
            return json_str
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
            return True
    except sqlite3.Error as e: 
        print(f"error: {e}")
        return False

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
            return True
    except sqlite3.Error as e: 
        print(f"error: {e}")
        return False

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
            return True
    except sqlite3.Error as e: 
        print(f"error: {e}")
        return False