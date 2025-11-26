
class Employee:
    language = "Py" # This is a class attribute 
    salary = 1200000

    def __init__(self, name, salary, language): # Dunder methid which automatically called when an function is created
        self.name = name
        self.salary = salary
        self.language = language 
        print("I am creating an object")
     

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

kamran = Employee("Kamran", 140000, "Python")
kamran.name = "Kamran"

print (kamran.name, kamran.salary,kamran.language)
