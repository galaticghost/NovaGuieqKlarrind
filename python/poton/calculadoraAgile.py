import pytest

#Soma
def add(n1,n2 : float) -> float:
    return n1 + n2    

#Subtrai
def subtract(n1,n2 : float) -> float:
    return n1 - n2

#multiplica
def multiplicacao(n1,n2 : float) -> float:
    return n1 * n2

#divide
def divisao(n1,n2 : float) -> float:
    if n2 == 0:
        return ZeroDivisionError
    return n1/n2

#Testa soma
def test_add():
    assert add(2,3) == 5
    assert add(2.3, 2.3) == 4.6
    assert add(0, -1) == -1

#Testa subtração
def test_subtract():
    assert subtract(3,5) == -2
    assert subtract(5.3, 5.1) == 0.2

def test_multiplicacao():
    assert multiplicacao(2,3) == 6
    assert multiplicacao(2, 1.5) == 3

def test_divisao():
    assert divisao(4,2) == 2
    assert divisao(4,0) == ZeroDivisionError
    assert divisao(0,4) == 0
    assert divisao(3,1) == 3
    assert divisao(3,2) == 1.5
    assert divisao(5,3) == 1.6666666666666667