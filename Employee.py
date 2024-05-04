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