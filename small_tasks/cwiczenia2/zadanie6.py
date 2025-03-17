prices = {
    "jajka": 7.69,
    "mleko": 3.49,
    "ser": 15.99,
    "chleb": 4.74,
    "masło": 5.76,
    "mąka": 2.99
}

a = ["ser", "ser", "jajka", "mąka", "mąka", "mąka", "mleko", "chleb", "masło"]

def koszt(ceny, lista):
    koszt = 0
    for produkt in lista:
        cena = ceny.get(produkt)
        koszt += cena
    return koszt

result = koszt(prices, a)

print(result)