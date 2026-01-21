class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):\
    print(f"Out of all langauge here is your language {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
         print(f"The name is {self.company} and he is good with {self.language}")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()