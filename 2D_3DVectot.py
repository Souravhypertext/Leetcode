class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"This vector is {self.i}i {self.j}j ")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"This vector is {self.i}i {self.j}j {self.k}k")

a = TwoDVector(1,2)
a.show()
b = ThreeDVector(3,4,5)
b.show()




