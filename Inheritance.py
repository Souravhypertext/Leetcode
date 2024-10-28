class Employee():
    company = "Google"

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary of Employee is{self.salary}")

class Programmer(Employee):
    company = "Alphabet"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} Language")

a = Employee()
b =Programmer()

print(a.company,b.company)
