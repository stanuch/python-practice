data_output = open("zad2_output.txt", "w")

def liczba_pierwsza(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

liczby_pierwsze = [x for x in range(201) if liczba_pierwsza(x)]

for liczba in liczby_pierwsze:
    data_output.write(f"{str(liczba)}\n")

data_output.close()