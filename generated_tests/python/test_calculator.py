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
    (-1, 1, '-', -2),
    (0, 0, '-', 0),
    (10, 5, '*', 50),
    (-1, -1, '*', 1),
    (0, 0, '*', 0),
    (10, 5, '/', 2),
    (-10, -5, '/', 2),
    (0, 1, '/', 0),
])
def test_calculator_normal_cases(a, b, operation, expected):
    """Test calculator with normal inputs."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 0, '/', "Error: Division by zero is not allowed."),
    (1.2, 0.6, '/', 2),
    ('a', 5, '+', "Error: Invalid operation."),
    (10, 'b', '-', "Error: Invalid operation."),
    (10, 5, 'x', "Error: Invalid operation."),
])
def test_calculator_edge_and_error_cases(a, b, operation, expected):
    """Test calculator with edge and error inputs."""
    assert calculator(a, b, operation) == expected

def test_calculator_division_by_zero():
    """Test division by zero specifically."""
    result = calculator(10, 0, '/')
    assert result == "Error: Division by zero is not allowed."

def test_calculator_invalid_operation():
    """Test calculator with an invalid operation."""
    result = calculator(10, 5, 'invalid')
    assert result == "Error: Invalid operation."

@pytest.mark.parametrize("a, b, operation", [
    (None, 5, '+'),
    (10, None, '-'),
    (None, None, '*'),
])
def test_calculator_with_none_as_input(a, b, operation):
    """Test calculator when None is passed as an argument."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)