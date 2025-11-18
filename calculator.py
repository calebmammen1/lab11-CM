# https://github.com/calebmammen1/lab11-CM.git
# Partner 1: Caleb Mammen
# Partner 2: Caleb Mammen

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    if (a <= 0 or a == 1 or b <= 0):
        raise ValueError("Invalid logarithm arguments.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hyp(a, b):
    return math.hypot(a, b)
