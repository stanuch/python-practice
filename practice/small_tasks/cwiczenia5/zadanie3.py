class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
        
    def perimeter(self):
        return (2 * self.a) + (2 * self.b)

    def diagonal(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def __repr__(self):
        return "Bok 'a' prostokąta ma długość {}, a bok 'b' ma długość {}. Obwód wynosi {}, a jego przekątna to {}. Powierzchnia wynosi {}".format(self.a, self.b, self.perimeter(), self.diagonal(), self.area())

a = Rectangle(5, 3)

print(a.area())
print(a.perimeter())
print(a.diagonal())

print(a)