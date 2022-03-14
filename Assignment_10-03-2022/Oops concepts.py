class Quadlilateral:
    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def Perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4
    def PrintSide(self):
        print("Side1-", self.s1)
        print("Side2-", self.s2)
        print("Side3-", self.s3)
        print("Side4-", self.s4)

class Rectangle(Quadlilateral):
    def __init__(self, a, b):
        Quadlilateral.__init__(self,a, b, a, b)

    def area(self):
        return self.s1*self.s2
    def PrintSide(self):
        print("Side1-", self.s1)
        print("Side2-", self.s2)

class Square(Rectangle):
    def __init__(self, a):
        Rectangle.__init__(self,a, a)
    def PrintSide(self):
        print("Side-", self.s1)

S = Square(30)
print("Area of square is-", S.area())
print("Parameter of square is -", S.Perimeter())
print("Measurement of Square is- ")
S.PrintSide()
print("---------------------------------------------------------------")
R = Rectangle(20, 30)
print("Area of rectangle is-", R.area())
print("Parameter of rectangle is -", R.Perimeter())
print("Measurement of rectangle is- ")
R.PrintSide()
print("---------------------------------------------------------------")
Q = Quadlilateral(14, 32, 22, 14)
print("Parameter of quadrilateral is -", R.Perimeter())
print("Measurement of quadrilateral is- ")
Q.PrintSide()

