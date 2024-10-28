class Programmer:
    company = "Alphabet"

    def __init__(self,name,salary,position,location):
        self.name = name
        self.salary = salary
        self.position = position
        self.location = location

p = Programmer("Sourav",2000000,"senior software developer","Faroe Island")
print(p.name,p.salary,p.position,p.location)
r = Programmer("Ruchika",150000,"Product manager","Seattle")
print(r.name,r.salary,r.position,r.location)
