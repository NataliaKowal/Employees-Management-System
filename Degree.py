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
    with sqlite3.connect(DB_path) as con:
        cur = con.cursor()
        records = cur.execute("SELECT * FROM Degree").fetchall()
        print(records)
        degrees = []
        for record in records:
            degrees.append(Degree(record))

        for degree in degrees:
            print(degree)