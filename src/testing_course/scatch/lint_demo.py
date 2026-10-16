
import pytest

from testing_course.exploration.calculator import Calculator


def find(name: str | None, items=[]):
    if name == None:
        return False
    if name in items:
        return True
    else:
        return False

def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(1,0)

@pytest.mark.parametrize("x,y", [(1,2)])
def test_add(x,y):
    assert Calculator.add(x,y) ==3