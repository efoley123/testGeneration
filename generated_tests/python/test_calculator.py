import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 1, '+', 2),
    (-1, -1, '+', -2),
    (1.5, 2.5, '+', 4.0),
    (100, 50, '-', 50),
    (-1, 1, '-', -2),
    (1.2, 0.8, '-', 0.4),
    (10, 5, '*', 50),
    (0, 0, '*', 0),
    (-1, -1, '*', 1),
    (10, 2, '/', 5),
    (-10, 2, '/', -5),
    (10, 0, '/', "Error: Division by zero is not allowed."),
    (10, 5, 'x', "Error: Invalid operation."),
])
def test_calculator(a, b, operation, expected):
    """Test calculator with various operations and edge cases."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ("a", 1, '+'),
    (1, "b", '-'),
    ("a", "b", '*'),
])
def test_calculator_with_invalid_inputs(a, b, operation):
    """Test calculator with invalid inputs to ensure it doesn't break."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)