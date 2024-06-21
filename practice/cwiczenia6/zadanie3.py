uczniowie = {}

with open("zad3.txt", "r") as data:
    for line in data:
        info = line.split(":")
        imie_nazwisko = info[0]
        lista_ocen = info[1].split()
        oceny = [int(ocena) for ocena in lista_ocen]
        uczniowie[imie_nazwisko] = oceny

print(uczniowie)