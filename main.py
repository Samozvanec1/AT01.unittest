
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def check(a):
    return a % 2 == 0

def divide_zero(a, b):
    if b == 0:
        raise TypeError('Деление на ноль невозможно')
    return a / b
