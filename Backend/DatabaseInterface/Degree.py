import sqlite3

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


def list_degrees (DB_path):
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            records = cur.execute("SELECT * FROM Degree").fetchall()
            degrees = []
            for record in records:
                degree = Degree(record)
                print(degree)
                degrees.append(degree)
                
    except sqlite3.Error as e: 
        print(f"error: {e}")

def add_degree (DB_path, name):
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Degree (Name) VALUES (?)", (name, ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")

def edit_degree (DB_path, name, Id):
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("UPDATE Degree SET Name = ? WHERE Id = ?", (name, Id,  ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")

def delete_degree (DB_path, Id):
    try: 
        with sqlite3.connect(DB_path) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Degree WHERE Id = ?", (Id, ))
            con.commit()
    except sqlite3.Error as e: 
        print(f"error: {e}")