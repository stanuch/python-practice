def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

OPERATIONS = {"add": add, "sub": sub, "mul": mul, "div": div}

def make_operation(a, b, opcode):
        operation = OPERATIONS[opcode]
        wynik = operation(a, b)
        print(wynik)

# task:
program = [(5.43, 2.43, "add"), (3, 2, "sub"), (21, 7, "div"), (6.54, 2.81, "mul")]

# exec:
for a, b, opcode in program:
    make_operation(a, b, opcode)