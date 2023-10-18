text = "Jestem studentem Uniwersytetu Jagiellońskiego!"

znaki = ["-", ",", ".", "'", "!", "?"]

for znak in znaki:
    text = text.replace(znak, "")

def ilosc_liter(text):
    dict = {}
    words = text.split()

    for word in words:
        dict[word] = len(word)
    return dict

result = ilosc_liter(text)

print(result)