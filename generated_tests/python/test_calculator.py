import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, '+', 15),  # Normal case addition
    (1, 2, '-', -1),  # Normal case subtraction
    (3, 4, '*', 12),  # Normal case multiplication
    (10, 2, '/', 5),  # Normal case division
    (10, 0, '/', "Error: Division by zero is not allowed."),  # Division by zero
    (10, 5, '%', "Error: Invalid operation."),  # Invalid operation
    (0, 0, '+', 0),  # Edge case with zeros for addition
    (0, 0, '-', 0),  # Edge case with zeros for subtraction
    (0, 0, '*', 0),  # Edge case with zeros for multiplication
    (0, 0, '/', "Error: Division by zero is not allowed."),  # Edge case with zeros for division
])
def test_calculator(a, b, operation, expected):
    """Test calculator function with various operations including edge cases and error handling."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation, expected_exception", [
    ('a', 5, '+', TypeError),  # Non-integer addition
    (10, 'b', '-', TypeError),  # Non-integer subtraction
    (None, 4, '*', TypeError),  # None multiplication
    (10, None, '/', TypeError),  # None division
])
def test_calculator_exceptions(a, b, operation, expected_exception):
    """Test calculator function with inputs that should raise exceptions."""
    with pytest.raises(expected_exception):
        calculator(a, b, operation)