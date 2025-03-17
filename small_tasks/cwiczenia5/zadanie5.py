class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "{}, age: {}".format(self.name, self.age)


a = [
    Person("Krzysztof", 38),
    Person("Joanna", 45),
    Person("Paweł", 23),
    Person("Agnieszka", 19),
    Person("Michał", 24),
    Person("Dominika", 27)
]

a_sorted = sorted(a, key = lambda elem: elem.name)

print(a_sorted)