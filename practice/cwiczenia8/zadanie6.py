import re

txt = "kot 05-23-1985 kanarek 07-21-2011 rybki 12-25-2023 pies"
pattern = "[0-9]{2}-[0-9]{2}-[0-9]{4}"

result = re.findall(pattern, txt)

lista = []

for date in result:
    fields = date.split("-")
    poprawna_data = fields[1] + "-" + fields[0] + "-" + fields[2]
    lista.append(poprawna_data)

print(f"Daty w formacie MM-DD-YYYY: {result}")
print(f"Daty w formacie DD-MM-YYYY: {lista}")