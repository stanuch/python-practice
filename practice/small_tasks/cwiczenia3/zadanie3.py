# Napisz listę składaną zawierającą tylko wyrazy (z napisu a) rozpoczynające się od samogłoski.

a = "Nauka jest jak klucz do tajemniczego zamku wiedzy, otwierający przed nami drzwi do nieustannie rozwijającego się świata, gdzie każde odkrycie to kolejny krok w kierunku głębszego zrozumienia naszego otoczenia i samego siebie."

vowels = {"a", "e", "i", "y", "o", "u"}

a_małe = a.lower()
a_słowa = a_małe.split()

słowa = [word for word in a_słowa if word[0] in vowels]

print(słowa)

# Nie wiem czy "i" mozna nazwac słowem :P