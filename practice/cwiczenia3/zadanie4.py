#Napisz listę składaną przypisująca wartość func_a(x) dla x parzystych i func_b(x) dla x nieparzystych. 0 < x < 10

func_a = lambda x: x * 3.14
func_b = lambda x: x / 17

list = [func_a(liczba) if liczba % 2 == 0 else func_b(liczba) for liczba in range(1,10)]

print(list)