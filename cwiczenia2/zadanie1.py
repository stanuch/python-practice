def wielomian(x):
    wynik_wielomianu = 3*x**3 - 2*x**2 + 7*x - 12
    return wynik_wielomianu

x = int(input(f"Podaj liczbę 'x': "))

wynik_wielomianu = wielomian(x)

print(f"Wynik wielomianu dla x = {x}: {wynik_wielomianu}")