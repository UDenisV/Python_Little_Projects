import main

def test_is_factor1():
    if main.is_factor(3, 12) == True:
        print("Test is_factor(a, b) is OK")
    else:
        print("Test is_factor(a, b) is Fail")
    print("Result:", main.is_factor(3, 12))
    print()

def test_is_factor2():
    if main.is_factor(4, 7) == False:
        print("Test is_factor(a, b) is OK")
    else:
        print("Test is_factor(a, b) is Fail")
    print("Result:", main.is_factor(4, 7))
    print()

def test_is_mulltiple1():
    if main.is_mulltiple(15, 5) == True:
        print("Test is_mulltiple(a, b) is OK")
    else:
        print("Test is_mulltiple(a, b) is Fail")
    print("Result:", main.is_mulltiple(15, 5))
    print()

def test_is_mulltiple2():
    if main.is_mulltiple(9, 5) == False:
        print("Test is_mulltiple(a, b) is OK")
    else:
        print("Test is_mulltiple(a, b) is Fail")
    print("Result:", main.is_mulltiple(9, 5))
    print()

def test_num_digits():
    if main.num_digits(100) == 3:
        print("Test num_digits(a) is OK")
    else:
        print("Test num_digits(a) is Fail")
    print("Result:", main.num_digits(100))
    print()

def test_is_prime():
    if main.is_prime(11) == True:
        print("Test is_prime(a) is OK")
    else:
        print("Test is_prime(a) is Fail")
    print("Result:", main.is_prime(3))
    print()

def test_sum_of_squares_of_digits():
    if main.sum_of_squares_of_digits(987) == 194:
        print("Test sum_of_squares_of_digits(a) is OK")
    else:
        print("Test sum_of_squares_of_digits(a) is Fail")
    print("Result:", main.sum_of_squares_of_digits(987))
    print()

test_is_factor1()
test_is_factor2()
test_is_mulltiple1()
test_is_mulltiple2()
test_num_digits()
test_is_prime()
test_sum_of_squares_of_digits()
