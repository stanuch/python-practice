import random

def odleglosc(x1, y1, x2, y2):
    """Wyznacza długość pomiędzy dwoma punktami w przestrzeni dwuwymiarowej."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def fibo(x):
    if x == 0: 
        return 0
    elif x == 1:
        return 1
    p, w = 0, 1
    for i in range(x-1):
        p, w = w, p+w
    return w

def rng(x):
    return random.uniform(0.0, x)