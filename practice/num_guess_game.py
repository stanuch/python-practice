import random

liczba = random.randint(0,100)

podana = input("Enter a whole number between 1 and 100: ")
x = int(podana)

while x != liczba:
    if x < liczba:
        print("The generated number is greater than yours, please try again!")
        podana = input("\nEnter an integer: ")
        x = int(podana)
    if x > liczba:
        print("The generated number is smaller than yours, please try again!")
        podana = input("\nEnter an integer: ")
        x = int(podana)
else:
    print(f"\nCongratulations. You guessed the right number: '{liczba}'")