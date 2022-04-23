import calc

def test_add():
    if calc.add(1, 2) == 3:
        print("Test add(a, b) is OK")
    else:
        print("Test add(a, b) is Fail")
    print("Result:", calc.add(1, 2))
    print()

def test_sub():
    if calc.sub(4, 2) == 2:
        print("Test sub(a, b) is OK")
    else:
        print("Test sub(a, b) is Fail")
    print("Result:", calc.sub(4, 2))
    print()

def test_mul():
    if calc.mul(2, 5) == 10:
        print("Test mul(a, b) is OK")
    else:
        print("Test mul(a, b) is Fail")
    print("Result:", calc.mul(2, 5))
    print()

def test_div():
    if calc.div(8, 4) == 2:
        print("Test div(a, b) is OK")
    else:
        print("Test div(a, b) is Fail")
    print("Result:", calc.div(8, 4))
    print()

def test_sqr():
    if calc.sqr(4) == 2:
        print("Test sqr(a) is OK")
    else:
        print("Test sqr(a) is Fail")
    print("Result:", calc.sqr(4))
    print()
        
def test_pov():
    if calc.pov(2, 4) == 16:
        print("Test pov(a, b) is OK")
    else:
        print("Test pov(a, b) is Fail")
    print("Result:", calc.pov(2, 4))
    print()

def test_compare1():
    if calc.compare(10, 5) == 1:
        print("Test compare1(a, b) is OK")
    else:
        print("Test compare1(a, b) is Fail")
    print("Result:", calc.compare(10, 5))
    print()

def test_compare2():
    if calc.compare(4, 8) == -1:
        print("Test compare2(a, b) is OK")
    else:
        print("Test compare2(a, b) is Fail")
    print("Result:", calc.compare(4, 8))
    print()

def test_compare3():
    if calc.compare(6, 6) == 0:
        print("Test compare3(a, b) is OK")
    else:
        print("Test compare3(a, b) is Fail")
    print("Result:", calc.compare(6, 6))
    print()
        
def test_compare4():
    if calc.compare(-8, 1) == -1:
        print("Test compare4(a, b) is OK")
    else:
        print("Test compare4(a, b) is Fail")
    print("Result:", calc.compare(-8, 1))
    print()

test_add()
test_sub()
test_mul()
test_div()
test_sqr()
test_pov()
test_compare1()
test_compare2()
test_compare3()
test_compare4()