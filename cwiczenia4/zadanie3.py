# Napisz odpowiednik programu podanego w zadaniu, używający funkcji wbudowanych map i filter.

data = {
    "kot": 43,
    "pies": 29,
    "kanarek": 12,
    "rybki": 73,
    "chomik": 32,
}

data_alter = list(map(lambda elem: (elem[0].upper(), (elem[1] / 2) ** 2), data.items())) # Zmapowanie funkcji na wszystkie elementy "data"

data_filtered = list(filter(lambda elem: elem[1] > 300, data_alter)) # Odfiltrowanie tylko tych wyrazów które mają przypisaną wartość wiekszą od 300

print(data_filtered)