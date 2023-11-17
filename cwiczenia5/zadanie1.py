class Polynomial:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate(self, x):
        return self.a * x ** 3 + self.b * x ** 2 + self.c * x + self.d
    
wielomian = Polynomial(2, 3, 1, 4)

x = 4

result = wielomian.evaluate(x)

print(f"Wynik dla x = {x}: {result}")