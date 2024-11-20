import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, '+', 15),
    (-1, -1, '+', -2),
    (0, 0, '+', 0),
    (10, 5, '-', 5),
    (-1, -1, '-', 0),
    (0, 0, '-', 0),
    (10, 5, '*', 50),
    (-1, -1, '*', 1),
    (0, 0, '*', 0),
    (10, 2, '/', 5),
    (-1, -1, '/', 1),
    (10, 0, '/', "Error: Division by zero is not allowed."),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test calculator function with normal and edge cases."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    (10, 5, 'x'),
    (1, 2, ''),
    (10, 2, ' '),
])
def test_calculator_invalid_operation(a, b, operation):
    """Test calculator function with invalid operation."""
    assert calculator(a, b, operation) == "Error: Invalid operation."

# No explicit setup/teardown functions are necessary for this simple function testing