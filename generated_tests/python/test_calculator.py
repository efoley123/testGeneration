import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, '+', 15),
    (10, 5, '-', 5),
    (10, 5, '*', 50),
    (10, 5, '/', 2),
    (10, 0, '/', "Error: Division by zero is not allowed."),
    (10, 5, '%', "Error: Invalid operation."),
    (0, 0, '+', 0),
    (-1, -1, '+', -2),
    (-1, 1, '*', -1),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Test calculator function with normal, edge, and error cases.
    """
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    (None, 5, '+'),
    ('a', 5, '+'),
    (10, 'b', '-'),
    ([], {}, '*'),
])
def test_calculator_failure_cases(a, b, operation):
    """
    Test calculator function with inputs that should raise TypeError.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

def test_calculator_division_by_zero():
    """
    Test calculator function specifically for division by zero error message.
    """
    assert calculator(10, 0, '/') == "Error: Division by zero is not allowed."

def test_calculator_invalid_operation():
    """
    Test calculator function with an invalid operation to ensure the error message is returned.
    """
    assert calculator(10, 5, 'invalid_operation') == "Error: Invalid operation."