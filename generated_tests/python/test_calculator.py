import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, '+', 15),
    (10, 5, '-', 5),
    (10, 5, '*', 50),
    (10, 5, '/', 2.0),
    (10, 0, '/', "Error: Division by zero is not allowed."),
    (10, 5, '%', "Error: Invalid operation."),
    # Edge cases
    (0, 0, '+', 0),
    (-1, -1, '+', -2),
    (-1, 1, '-', -2),
    (1, -1, '*', -1),
    # Big numbers
    (1000000, 1000000, '+', 2000000),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test calculator function with normal and edge cases."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    (None, 5, '+'),
    ('a', 5, '+'),
    (10, 'b', '-'),
    ([], {}, '*'),
])
def test_calculator_error_cases(a, b, operation):
    """Test calculator function with error cases where inputs are not numbers."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)

def test_calculator_division_by_zero():
    """Test calculator function specifically for division by zero error."""
    result = calculator(10, 0, '/')
    assert result == "Error: Division by zero is not allowed."

def test_calculator_invalid_operation():
    """Test calculator function with an invalid operation."""
    result = calculator(10, 5, 'invalid_operation')
    assert result == "Error: Invalid operation."