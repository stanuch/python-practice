# Napisz program wyznaczający zbiór liter znajdujących się w napisie a ale nie w napisie b (wielkość liter nie powinna mieć znaczenia):

a = "Programowanie w Pythonie"
b = "Wielomian trzeciego stopnia"

a_duze = a.upper() # Zmiana liter na duze
b_duze = b.upper()

a_set = set(a_duze) # Utworzenie zbiorów z podanych tekstów
b_set = set(b_duze)

result = a_set.difference(b_set) # Działania na zbiorach

print("Zbiór liter znajdujących się w napisie a ale nie w napisie b, to:", result)