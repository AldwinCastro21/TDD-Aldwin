import pytest

class Calculator:
    def add(self, a, b):
        return abs(a + b)
        

calc = Calculator()

def test_answer_1():
    assert calc.add(1,1) == 2

def test_answer_2():
    assert calc.add(1.0,2.5) == 3.5

def test_answer_3():
    assert calc.add(0,0) == 0

def test_answer_4():
    assert calc.add(-6,-5) == 11


print(calc.add(1, 1))