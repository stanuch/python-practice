def wielomian(x):
    return 3*x**3 - 2*x**2 + 7*x - 12

x = int(input(f"Podaj liczbę 'x': "))

wynik_wielomianu = wielomian(x)

print(f"Wynik wielomianu dla x = {x}: {wynik_wielomianu}")
