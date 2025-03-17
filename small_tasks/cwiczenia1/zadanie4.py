lista = [0, 1]

def fibonacci(x):
    for x in range(2, x):
        lista.append(lista[-1] + lista[-2])
    return lista

ciąg = fibonacci(20)

print(ciąg)