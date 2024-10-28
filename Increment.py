class Employee:
    salary = 234
    increment = 20

    @property
    def salary_after_increment(self):
        return self.salary + self.increment * (self.increment/100)

    @salary_after_increment.setter

    def salary_after_increment(self,salary):
        self.increment = ((salary/self.salary)-1)*100


e = Employee()
print(e.salary_after_increment)
e.salary_after_increment = 2999
print(e.increment)


