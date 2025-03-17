def liczba_pierwsza(x):
    if x <= 1:
        return False
    
    for dzielnik in range(2, int(x ** 0.5) + 1):
        if x % dzielnik == 0:
            return False
    
    return True

x = int(input(f"Enter your number: "))

if liczba_pierwsza(x):
    print(f"Number {x} is prime :)")
else:
    print(f"Number {x} is not prime!")
