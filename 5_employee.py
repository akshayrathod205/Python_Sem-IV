class Employee:
    def __init__(self, fname, lname, age, basic):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.basic = basic
        self.email = fname + "." + lname + "@gmail.com"
        
    def display(self):
        print(f"Name: {self.fname} {self.lname}")
        print(f"Age: {self.age} \nSalary: {self.basic}")
        print(f"Email: {self.email}")
        
class Developer(Employee):
    def __init__(self, fname, lname, age, basic, lang):
        super().__init__(fname, lname, age, basic)
        self.lang = lang
        
    def display(self):
        super().display()
        print(f"Language: {self.lang}")
        
class Manager(Employee):
    def __init__(self, fname, lname, age, basic):
        super().__init__(fname, lname, age, basic)
        self.subordinates = []
        
    def addEmployee(self, newEmp):
        self.subordinates.append(newEmp)
        print(f"{newEmp.fname} {newEmp.lname} added as a subordinate")
        
    def display(self):
        super().display()
        if not self.subordinates:
            print("No subordinates")
        else:
            for newEmp in self.subordinates:
                print(f"Subordinates: {newEmp.fname} {newEmp.lname}")
        
emp2 = Developer("Jay", "Mor", 21, 10000, "Python")        
emp1 = Manager("Ram", "Shah", 20, 40000)
emp2.display()
emp1.addEmployee(emp2)
emp1.display()
