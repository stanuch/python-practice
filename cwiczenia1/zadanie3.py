text = "To Izma - królweski doradca . Żywy dowód, że kiedyś po ziemi stąpały dinozaury ."

znaki = ["-", ",", "."]

for znak in znaki:
    text = text.replace(znak, "")

words = text.split()
words_length={}

for word in words:
    word_upper = word.upper()
    words_length[word_upper] = len(word_upper)

print(words_length)