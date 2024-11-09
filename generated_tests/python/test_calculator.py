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
    (-10, -5, '+', -15),
    (-10, 5, '-', -15),
    (10, -5, '*', -50),
    (10, -2, '/', -5),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test calculator function with normal and edge cases."""
    result = calculator(a, b, operation)
    assert result == expected, f"Expected {expected}, got {result}"

@pytest.mark.parametrize("a, b, operation", [
    ("a", 5, '+'),
    (10, "b", '-'),
    ("a", "b", '*'),
])
def test_calculator_error_cases_with_non_numeric_inputs(a, b, operation):
    """Test calculator function with non-numeric inputs to ensure it raises TypeError."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)

def test_calculator_division_by_zero_error_message():
    """Test calculator function specifically for division by zero error message."""
    result = calculator(10, 0, '/')
    assert result == "Error: Division by zero is not allowed.", "Division by zero should return a specific error message."

@pytest.mark.parametrize("a, b, operation", [
    (1e10, 1e10, '+'),
    (-1e10, -1e10, '-'),
    (1e10, 1e-10, '*'),
    (1e-10, 1e10, '/'),
])
def test_calculator_with_large_numbers(a, b, operation):
    """Test calculator function with very large and very small numbers to check for overflow or underflow."""
    # No specific assertion for output, just checking that it doesn't raise an unexpected exception
    try:
        calculator(a, b, operation)
    except Exception as e:
        pytest.fail(f"Unexpected exception with large numbers: {e}")