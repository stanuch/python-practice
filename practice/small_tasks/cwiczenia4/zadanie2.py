# Znajdź wartości mniejsze od zera dla w(x), gdzie 0 <= x < 10. Użyj map i filter.

def wielomian(x):
    return x ** 2 - 4 * x + 2

x = range(0,10)

wyniki = list(map(wielomian, x)) # Zmapowanie funckji wielomianu na dany x (range(0,10)) i utworzenie listy

filtered = list(filter(lambda result: result < 0, wyniki)) # Filtrowanie wyników które są mniejsze od zera

print("Wartości mniejsze od zera dla w(x), w zakresie od 0 do 9:", filtered)