from math import sqrt


def add(a, b):
    return a + b
def sub(a, b):
    return a-b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def sqr(a):
    return sqrt(a)
def pov(a, b):
    return pow(a, b)
def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1