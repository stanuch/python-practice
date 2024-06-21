import random
import time

buffer = [random.uniform(0.0, 10.0) for _ in range(1000000)]


def a(buffer):
    return [x ** 2 for x in buffer]


def b(buffer):
    new_buffer = []

    for x in buffer:
        new_buffer.append(x ** 2)

    return new_buffer

start1 = time.time()
result1 = a(buffer)
end1 = time.time()

start2 = time.time()
result2 = b(buffer)
end2 = time.time()

delta1 = end1 - start1
delta2 = end2 - start2

delta1 = float(delta1)
delta2 = float(delta2)

if delta1 < delta2:
    print("Szybciej wykonała się funkcja 'a'")
    print("Szybciej o:", (delta2 - delta1), "sekundy.")
else:
    print("Szybciej wykonała się funkcja 'b'")
    print("Szybciej o:", (delta1 - delta2), "sekundy.")