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
    (-10, -5, '+', -15),
    (1.5, 0.5, '+', 2.0),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Test normal and edge cases for calculator function.
    """
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ('a', 5, '+'),
    (10, 'b', '-'),
    ('a', 'b', '*'),
])
def test_calculator_with_invalid_inputs(a, b, operation):
    """
    Test calculator function with invalid input types to ensure it doesn't crash.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

@pytest.mark.parametrize("a, b, operation", [
    (10, 0, '/'),
    (0, 0, '/'),
])
def test_calculator_division_by_zero(a, b, operation):
    """
    Test division by zero scenarios for calculator function.
    """
    assert calculator(a, b, operation) == "Error: Division by zero is not allowed."

@pytest.mark.parametrize("a, b, operation", [
    (10, 5, '%'),
    (10, 5, '^'),
    (10, 5, 'invalid_operation'),
])
def test_calculator_invalid_operation(a, b, operation):
    """
    Test calculator function with invalid operations.
    """
    assert calculator(a, b, operation) == "Error: Invalid operation."