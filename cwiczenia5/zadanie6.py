class Kwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def pierwiastki(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta < 0:
            return "Równanie nie posiada pierwiastków."
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return f"Pierwiastek równania wynosi: {x}"
        else:
            x1 = (-self.b - (delta ** 0.5)) / (2 * self.a)
            x2 = (-self.b + (delta ** 0.5)) / (2 * self.a)
            return f"Pierwiastki równania wynoszą: {x1} i {x2}"

    def wartosc(self, x):
        return (self.a ** 2 * x) + (self.b * x) + (self.c) 

a = 3
b = 8
c = 2
x = 5

funkcja = Kwadratowa(a, b, c)

print(f"Wartość równania dla '{x}': {funkcja.wartosc(x)}")
print(f"Delta tego równania wynosi: {funkcja.delta()}")
print(funkcja.pierwiastki())
