# Oblicz odchylenie standardowe liczb znajdujących się w liście a. Użyj funkcji wbudowanych map, sum oraz len.

a = [6.43, 1.44, 8.35, 8.32, 2.98, 3.34, 7.17, 4.32, 9.76, 2.34, 6.54, 1.78, 2.76]

def funkcja_średnia(x):
    return sum(x)/len(x)
średnia = funkcja_średnia(a)

nawiasy = list(map(lambda x: (x - średnia) ** 2, a))

odchylenie = (sum(nawiasy) / len(a)) ** 0.5

print("Odchylenie standardowe wynosi:", odchylenie)