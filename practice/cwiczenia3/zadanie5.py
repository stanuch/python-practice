#Napisz listę składaną zawierającą 10 pierwszych elementów ciągu Fibonacciego (można zdefiniować funkcję pomocniczą).

def fibonacci(x):
    list = [0, 1]
    for x in range(2, x):
        list.append(list[-1] + list[-2])
    return list

x = 10 # Liczba pierwszych elementów które chcemy uzyskać

lista = [fibonacci(number) for number in range(0, x+1)] # "x+1" aby 10. element był inkluzywny

print(lista[-1]) # Nie wiedziałem czy mam wyświetlić wszystkie listy po kolei czy tylko tą zawierającą 10 elementów