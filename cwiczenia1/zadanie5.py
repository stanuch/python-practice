def liczba_pierwsza(x):
    if x <= 1:
        return False
    
    for dzielnik in range(2, int(x ** 0.5) + 1):
        if x % dzielnik == 0:
            return False
    
    return True

x = int(input(f"Proszę podać liczbę: "))

if liczba_pierwsza(x):
    print(f"Liczba {x} jest pierwsza :)")
else:
    print(f"Liczba {x} nie jest pierwsza!")
