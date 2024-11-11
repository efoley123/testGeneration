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
    (10, 5, 'invalid', "Error: Invalid operation."),
    # Edge cases
    (0, 0, '+', 0),
    (-1, -1, '+', -2),
    (-1, 1, '-', -2),
    (1.5, 2.5, '+', 4.0),
    # Large numbers
    (1e10, 1e10, '+', 2e10),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test normal and edge cases for the calculator function."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ("string", 5, '+'),
    (10, "string", '-'),
    (None, 5, '*'),
    (10, None, '/'),
])
def test_calculator_error_cases(a, b, operation):
    """Test error cases for the calculator function with invalid inputs."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)

@pytest.mark.parametrize("a, b, expected_error", [
    (10, 0, ZeroDivisionError),
])
def test_calculator_division_by_zero(a, b, expected_error):
    """Test division by zero for the calculator function."""
    with pytest.raises(expected_error):
        calculator(a, b, '/')