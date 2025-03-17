import datetime

now = datetime.datetime.now()
grunwald = datetime.datetime(1410, 7, 15)

roznica = now - grunwald

dni = roznica.total_seconds() / 60 / 60 / 24

print(f"Liczba dni od dnia Bitwy pod Grunwaldem do teraz wynosi: {dni:.2f}")