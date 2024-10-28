class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hello, {self.name}")


p1 = Person("Sourav Kumar")
p1.talk()

p2 = Person("Gourav Kumar")
p2.talk()

p3 = Person("Sourav Choudhary")
p3.talk()