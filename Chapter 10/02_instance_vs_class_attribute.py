
class Employee:
    language = "Py" # This is a class attribute 
    salary = 1200000


kamran = Employee()
kamran.language = "Javascript" # This is a object attribute
print(kamran.language,kamran.salary)


# Here name is object attribute and salary and language are class attributes as tehy directly belong to the class 