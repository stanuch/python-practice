# Napisz funkcję wyznaczającą iloczyn liczb podanych przy pomocy argumentu z gwiazdką. Jeśli w wywołaniu, wśród argumentów trafi się wartość nie będąca liczbą, funkcja powinna zwrócić wartość None.

def iloczyn(*args):
    result = 1
    for arg in args:
        try:
            arg = float(arg) # Zmiana typu na float
            result *= arg
        except:
            return None # Jeśli nie uda się wykonać wcześniejszych poleceń, funkcja przyjmie wartość None
    return result

print(iloczyn(2, 4, 6, 3))
print(iloczyn(2, 3, 5, "pies"))