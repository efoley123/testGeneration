import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, '+', 8),
    (10, 5, '-', 5),
    (4, 6, '*', 24),
    (8, 2, '/', 4),
    (5, 0, '/', "Error: Division by zero is not allowed."),
    (1, 1, 'invalid', "Error: Invalid operation."),
    # Edge cases
    (0, 0, '+', 0),
    (-1, -1, '*', 1),
    (-5, 5, '/', -1),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test calculator function with normal and edge cases."""
    result = calculator(a, b, operation)
    assert result == expected, f"Expected {expected}, got {result}"

@pytest.mark.parametrize("a, b, operation", [
    ('a', 5, '+'),
    (10, 'b', '-'),
    (None, 6, '*'),
    ([], 2, '/'),
    (5, {}, '+'),
])
def test_calculator_error_cases(a, b, operation):
    """Test calculator function with invalid types to ensure it doesn't raise unexpected errors."""
    with pytest.raises((TypeError, ValueError)):
        calculator(a, b, operation)

def test_calculator_division_by_zero():
    """Test division by zero specifically to ensure proper error message."""
    result = calculator(10, 0, '/')
    assert result == "Error: Division by zero is not allowed.", f"Expected division by zero error, got {result}"

def test_calculator_invalid_operation():
    """Test invalid operation to ensure proper error message."""
    result = calculator(10, 5, 'invalid')
    assert result == "Error: Invalid operation.", "Expected invalid operation error, got {result}"