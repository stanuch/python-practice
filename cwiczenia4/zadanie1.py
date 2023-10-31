# Napisz program wypisujący długości kolejnych wyrazów z tekstu a, ale tylko wtedy gdy długości te są liczbami parzystymi. Ponadto, wyrazy powinny być pozbawione znaków interpunkcyjnych (trzeba usunąć przylegające przecinki i kropki). Użyj funkcji wbudowanych map, filter i zip.

a = """Van Rossum was born and raised in the Netherlands, where he received a master's degree in mathematics and computer science from the University of Amsterdam in 1982. He received a bronze medal in 1974 in the International Mathematical Olympiad. He has a brother, Just van Rossum, who is a type designer and programmer who designed the typeface used in the "Python Powered" logo."""

znaki = (",", ".", '"', "'") # Usunięcie znaków interpunkcyjnych
for znak in znaki:
    a = a.replace(znak, "")

words = a.split()

parzyste_słowa = filter(lambda word: len(word) % 2 == 0, words) # Odfiltrowanie słów które mają parzystą długość
parzyste_słowa_kopia = list(parzyste_słowa) # Zrobiłem kopię tego, zeby uniknąć tych problemów z nierówną iteracją

word_lengths = map(len, parzyste_słowa_kopia) # Zmapowanie funkcji "len" na dane słowa

result = zip(parzyste_słowa_kopia, word_lengths) # Połączenie słów i liczby liter w danym słowie

for words in result:
    print(words)