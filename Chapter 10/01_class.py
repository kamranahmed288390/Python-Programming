class Employee:
    language = "Py" # This is a class attribute 
    salary = 1200000


kamran = Employee()
kamran.name = "Kamran" # This is a object attribute
print(kamran.name,kamran.language,kamran.salary)

ahmed = Employee()
ahmed.name = "Ahmed"
print(ahmed.name,ahmed.language, ahmed.salary)


# Here name is object attribute and salary and language are class attributes as tehy directly belong to the class 