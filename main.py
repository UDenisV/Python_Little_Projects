def is_factor(a, b):
    if b%a == 0:
        return True
    else:
        return False

def is_mulltiple(a, b):
    if a%b == 0:
        return True
    else:
        return False

def num_digits(a):
    c = 0
    while a != 0:
        c += 1
        a = a // 10
    return c

def is_prime(a):
    c = 0
    for i in range(1, a+1):
        if a%i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

def sum_of_squares_of_digits(a):
    s = 0
    while a != 0:
        s += (a%10)**2
        a = a // 10
    return s