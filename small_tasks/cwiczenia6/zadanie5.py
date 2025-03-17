data = [
    {"a": [1, 2, 3], "b": "kot"},
    {1: "pies", 2: "kanarek"},
    [0, 1, 1, 2, 3, 5, 8, 13]
]

data_output = open("zad5_output.txt", "w")

for elem in data:
    data_output.write(f"{str(elem)}\n")

data_output.close()