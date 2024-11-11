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
    (-10, -5, '+', -15),
    (-10, 5, '-', -15),
    (0, 0, '+', 0),
    (0, 0, '*', 0),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test calculator function with normal and edge cases."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    (10, 5, 'x'),
    (10, 5, 'div'),
    (10, 5, '%'),
])
def test_calculator_invalid_operations(a, b, operation):
    """Test calculator function with invalid operations."""
    assert calculator(a, b, operation) == "Error: Invalid operation."

def test_calculator_division_by_zero():
    """Test division by zero specifically."""
    assert calculator(10, 0, '/') == "Error: Division by zero is not allowed."

@pytest.mark.parametrize("a, b, operation, expected", [
    ('10', 5, '+', "TypeError"),
    (10, '5', '-', "TypeError"),
    ([], 5, '*', "TypeError"),
    (10, {}, '/', "TypeError"),
])
def test_calculator_type_errors(a, b, operation, expected):
    """Test calculator function with types that should cause a TypeError."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)