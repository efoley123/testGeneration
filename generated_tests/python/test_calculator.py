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
    (-1, 1, '-', -2),
])
def test_calculator_operations(a, b, operation, expected):
    """Test calculator function with various operations and edge cases."""
    assert calculator(a, b, operation) == expected

def test_division_by_zero():
    """Test division by zero specifically to ensure proper error message."""
    assert calculator(10, 0, '/') == "Error: Division by zero is not allowed."

def test_invalid_operation():
    """Test calculator with an invalid operation to ensure proper error handling."""
    assert calculator(10, 5, 'invalid_op') == "Error: Invalid operation."

@pytest.mark.parametrize("a, b, operation", [
    ('a', 5, '+'),
    (10, 'b', '-'),
    ('a', 'b', '*'),
])
def test_calculator_with_non_numeric_inputs(a, b, operation):
    """Test calculator function with non-numeric inputs to ensure it doesn't crash."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)