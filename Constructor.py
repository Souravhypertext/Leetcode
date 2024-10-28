class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating a constructor")


    def getinfo(self):
        print(f"The language is {self.language} , The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


sourav = Employee("sourav",1300000,"C++")

print(sourav.name,sourav.salary,sourav.language)