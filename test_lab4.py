import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
        
calc = Calculator("Calc 1")

@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True

def test_lab4_test3():
    assert calc.subtract(0,0) == 0
    assert calc.subtract(-1,-2) == 1
    assert calc.subtract(2,4) == -2
    assert calc.subtract(4,2) == 2
    assert calc.subtract(2.5,3.5) == -1.0
    assert calc.subtract(3.5,2.5) == 1.0

def test_lab4_test4():
    assert calc.multiply(0,0) == 0
    assert calc.multiply(1,0) == 0
    assert calc.multiply(1,1) == 1
    assert calc.multiply(0,-1) == 0
    assert calc.multiply(3.2,5.4) == 17.28
    assert calc.multiply(5.4,3.2) == 17.28
    assert calc.multiply(-1,-1) == 1
    
    