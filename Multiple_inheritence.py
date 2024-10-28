class Employee:
    company = "Google"
    name = "Default name"

    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "python"

    def print_language(self):
        print(f"Out of all languages here is your language : {self.language}")

class Programmer(Employee,Coder):
    company = "Alphabet"

    def show_language(self):
        print(f"The name of company is {self.company} and he is good in {self.language} Language")

a = Employee()
b =Programmer()

b.show()
b.print_language()
b.show_language()