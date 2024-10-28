from random import randint

class Train:
    def __init__(self,train_no):
        self.train_no = train_no

    def book(self,fro,to):
        print(f"Ticket is book in Train_Num{self.train_no},from{fro},to{to}")

    def get_status(self):
        print(f"Train no : {self.train_no} is running on time ")

    def get_fare(self,fro,to):
        print(f"The ticket fare from {fro} to {to} is {randint(222,5555)}")

t= Train(22322)
t.book("Patna","Gwalior")
t.get_status()
t.get_fare("Gwalior","New Delhi")

