liczby = [1, 5, 2, 1, 6, 8, 2]

def średnia_arytmetyczna(lista):
    for element in lista:
        if type(element) not in (int, float):
            return None
    return sum(lista) / len(lista)
    
wynik = średnia_arytmetyczna(liczby)

print(wynik)