import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Test file: test_calculator.py

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
    (-1, 1, '-', -2),
    (1.5, 0.5, '*', 0.75),
    (1.5, 0.5, '/', 3),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Test calculator with normal and edge cases.
    """
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ("a", 5, '+'),
    (10, "b", '-'),
    ("a", "b", '*'),
])
def test_calculator_error_cases_type_error(a, b, operation):
    """
    Test calculator with inputs that should cause type error.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

@pytest.mark.parametrize("a, b, operation", [
    (None, 5, '+'),
    (10, None, '-'),
    (None, None, '*'),
])
def test_calculator_error_cases_none_type(a, b, operation):
    """
    Test calculator with None inputs to ensure it handles NoneType.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)