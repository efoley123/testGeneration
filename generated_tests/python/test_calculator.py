import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected_result", [
    (5, 3, '+', 8),
    (5, 3, '-', 2),
    (5, 3, '*', 15),
    (5, 3, '/', 5/3),
    (5, 0, '/', "Error: Division by zero is not allowed."),
    (5, 3, '%', "Error: Invalid operation."),
    # Edge cases
    (0, 0, '+', 0),
    (0, 0, '-', 0),
    (0, 0, '*', 0),
    (0, 0, '/', "Error: Division by zero is not allowed."),
    (-5, -3, '+', -8),
    (-5, -3, '-', -2),
    (-5, -3, '*', 15),
    (-5, -3, '/', 5/3),
])
def test_calculator_operations(a, b, operation, expected_result):
    """
    Test normal, edge, and error cases for calculator function.
    """
    assert calculator(a, b, operation) == expected_result

@pytest.mark.parametrize("a, b", [
    ("a", 3),
    (5, "b"),
    ("a", "b"),
])
def test_calculator_with_non_numeric_inputs(a, b):
    """
    Test calculator function with non-numeric inputs to ensure it raises a TypeError.
    """
    with pytest.raises(TypeError):
        calculator(a, b, '+')

@pytest.mark.parametrize("a, b, operation", [
    (1.1, 2.2, '+'),
    (2.5, 0.5, '-'),
    (2.5, 0.5, '*'),
    (2.5, 0.5, '/'),
])
def test_calculator_with_float_inputs(a, b, operation):
    """
    Test calculator function with float inputs to ensure correct operation.
    """
    if operation == '+':
        expected_result = a + b
    elif operation == '-':
        expected_result = a - b
    elif operation == '*':
        expected_result = a * b
    elif operation == '/':
        expected_result = a / b
    assert calculator(a, b, operation) == expected_result

def test_calculator_division_by_zero():
    """
    Test calculator function specifically for division by zero case.
    """
    assert calculator(5, 0, '/') == "Error: Division by zero is not allowed."