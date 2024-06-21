class Fib:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.current_element = 0

    def next(self):
        result = self.a
        next_a = self.b
        next_b = self.a + self.b
        self.a = next_a 
        self.b = next_b
        self.current_element += 1
        return result
        

fib = Fib()

print(fib.next() == 0)
print(fib.next() == 1)
print(fib.next() == 1)
print(fib.next() == 2)
print(fib.next() == 3)
print(fib.next() == 5)
print(fib.next() == 8)
print(fib.next() == 13)