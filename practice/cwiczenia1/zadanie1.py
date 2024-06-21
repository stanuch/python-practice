data = [34, -3.24, 98, 43, "zimorodek", None, 121, -73, 6.51, 4 + 7j, 2, 87, 32, 9.32, -30]

suma = 0

for element in data:
    if type(element) == int:
        suma += element

print(suma)
