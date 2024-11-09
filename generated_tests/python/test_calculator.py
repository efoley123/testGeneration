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
    (1.5, 2.5, '+', 4.0),
])
def test_calculator_normal_edge_cases(a, b, operation, expected):
    """Test normal and edge cases for the calculator function."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ("a", 5, '+'),
    (10, "b", '-'),
    (None, 5, '*'),
    ("ten", "five", '/'),
])
def test_calculator_input_errors(a, b, operation):
    """Test input errors for the calculator function."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)

@pytest.mark.parametrize("a, b, operation", [
    (float('inf'), 1, '+'),
    (1, float('inf'), '-'),
    (float('nan'), 1, '*'),
    (1, float('nan'), '/'),
])
def test_calculator_with_inf_nan(a, b, operation):
    """Test calculator function with infinity and NaN values."""
    result = calculator(a, b, operation)
    if operation in ['+', '-', '*']:
        assert result == float('inf') or result != result  # NaN does not equal itself
    else:
        assert isinstance(result, str) and "Error" in result

def test_calculator_division_by_zero_handling():
    """Test division by zero is handled correctly."""
    assert calculator(10, 0, '/') == "Error: Division by zero is not allowed."

def test_calculator_invalid_operation_handling():
    """Test invalid operations are handled correctly."""
    assert calculator(10, 5, 'invalid_op') == "Error: Invalid operation."