class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
        def bark(self):
            print("bark")

class Cat(Mammal):
        def meow(self):
            print("meow")


mammal1 = Dog()
mammal1.walk()
mammal1.bark()

mammal2 = Cat()
mammal2.walk()
mammal2.meow()