with open("zad1.txt", 'r+') as data:
    lines = [line.split() for line in data]
    lista = [x for x in lines]
    liczby_listy = [[float(num) for num in elem] for elem in lista]
    a = [x for sublist in liczby_listy for x in sublist]

średnia = sum(a) / len(a)

nawiasy = list(map(lambda x: (x - średnia) ** 2, a))

odchylenie = (sum(nawiasy) / len(a)) ** 0.5

print(f"Średnia z liczb wynosi: {średnia}")
print(f"Odchylenie standardowe liczb wynosi: {odchylenie}")