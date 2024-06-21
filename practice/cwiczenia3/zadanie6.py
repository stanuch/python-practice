#Napisz listę składaną zawierającą wszystkie liczby pierwsze mniejsze od 30 (można użyć funkcji z poprzednich ćwiczeń).

def liczba_pierwsza(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

liczby_pierwsze = [x for x in range(30) if liczba_pierwsza(x)]

print(liczby_pierwsze)
