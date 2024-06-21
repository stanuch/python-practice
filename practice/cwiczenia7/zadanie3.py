import random

liczba = random.randint(0,100)

podana = input("Wprowadź liczbę całkowitą z zakresu od 1 do 100: ")
x = int(podana)

while x != liczba:
    if x < liczba:
        print("Wygenerwowana liczba jest większa od twojej, spróbuj ponownie!")
        podana = input("\nWprowadź liczbę całkowitą: ")
        x = int(podana)
    if x > liczba:
        print("Wygenerwowana liczba jest mniejsza od twojej, spróbuj ponownie!")
        podana = input("\nWprowadź liczbę całkowitą: ")
        x = int(podana)
else:
    print(f"\nGratulacje! Udało ci się zgadnąć wygenerowaną liczbę która wynosiła '{liczba}'")