class programmer:
    company = "Microsoft"
    
    def __init__(self, name , salary, pin):
        self.name = name 
        self.salary= salary
        self.pin = pin
      

p = programmer("Kamran",140000, 24502)
print(p.name,p.salary,p.company)
a = programmer("Ahmed",140000, 24504)
print(a.name,a.salary,a.company)