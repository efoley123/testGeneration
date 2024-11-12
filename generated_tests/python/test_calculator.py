import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# test_calculator.py
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
    (-10, 5, '-', -15),
    (0, 0, '+', 0),
    (0, 0, '/', "Error: Division by zero is not allowed."),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test calculator function with normal and edge cases."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    (None, 5, '+'),
    ('a', 5, '+'),
    (10, 'b', '-'),
    (10, 5, None),
])
def test_calculator_error_cases(a, b, operation):
    """Test calculator function with error cases, expecting exceptions."""
    with pytest.raises((TypeError, ValueError)):
        calculator(a, b, operation)