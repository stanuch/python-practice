class DataBucket:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __hash__(self):
        return hash((self.a, self.b))

    def __eq__(self, other):
            return (self.a, self.b) == (other.a, other.b)

a = (1, 2, 3, 4)
b = "olek"

obiekt = DataBucket(a, b)

x = (1, 2, 3, 4)
y = "olek"

obiekt2 = DataBucket(x, y)

print(obiekt == obiekt2)

dictionary = {obiekt: "test1", obiekt2: "test2"}

print(dictionary[obiekt])
print(dictionary[obiekt2])