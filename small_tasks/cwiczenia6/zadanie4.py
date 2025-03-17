class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return "{} {}, age: {}".format(self.name, self.surname, self.age)
    
lista = []

with open("zad4.txt", "r") as file:
    for line in file:
        dane = line.split()
        person = Person(dane[0], dane[1], dane[2])
        lista.append(person)

sorted = sorted(lista, key=lambda x: x.surname)

data_output = open("zad4_output.txt", "w")

for osoba in sorted:
    data_output.write(f"{osoba}\n")

data_output.close()