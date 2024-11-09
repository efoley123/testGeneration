import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, '+', 15),
    (-1, -1, '+', -2),
    (0, 0, '+', 0),
    (10, 5, '-', 5),
    (-1, -1, '-', 0),
    (0, 0, '-', 0),
    (10, 5, '*', 50),
    (-1, -1, '*', 1),
    (0, 0, '*', 0),
    (10, 5, '/', 2),
    (-10, -5, '/', 2),
    (10, 0, '/', "Error: Division by zero is not allowed."),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Test normal and edge cases for calculator function.
    """
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    (1, 2, '%'),
    ('a', 'b', '+'),
    (None, None, '+'),
    (10, 5, None),
])
def test_calculator_error_cases(a, b, operation):
    """
    Test error cases for calculator function.
    """
    assert calculator(a, b, operation) == "Error: Invalid operation."

def test_calculator_division_by_zero():
    """
    Test division by zero scenario separately.
    """
    assert calculator(10, 0, '/') == "Error: Division by zero is not allowed."