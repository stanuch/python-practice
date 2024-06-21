import re

txt = "https://pl.wikipedia.org/wiki/Wyra%C5%BCenie_regularne kot pies kanarek https://pl.wikipedia.org/wiki/Gramatyka_regularna rybki"

pattern = "https*://[^ ]*"
result = re.findall(pattern, txt)

print(result)