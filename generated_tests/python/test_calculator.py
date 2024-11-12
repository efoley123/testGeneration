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
    (10, -5, '/', -2),
    (-10, -5, '*', 50),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test calculator function with normal and edge cases."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ('a', 5, '+'),
    (10, 'b', '-'),
    ('a', 'b', '*'),
])
def test_calculator_error_cases_with_non_numeric_input(a, b, operation):
    """Test calculator function raises TypeError for non-numeric inputs."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)

@pytest.mark.parametrize("a, b, operation", [
    (None, 5, '+'),
    (10, None, '-'),
    (None, None, '*'),
])
def test_calculator_error_cases_with_none_input(a, b, operation):
    """Test calculator function raises TypeError for None inputs."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)

@pytest.mark.parametrize("a, b, operation", [
    (float('inf'), 5, '+'),
    (10, float('-inf'), '-'),
    (float('inf'), float('-inf'), '*'),
])
def test_calculator_with_infinity(a, b, operation):
    """Test calculator function with infinity values."""
    if operation == '/' and b == 0:
        assert calculator(a, b, operation) == "Error: Division by zero is not allowed."
    else:
        assert type(calculator(a, b, operation)) is float

@pytest.mark.parametrize("a, b, operation", [
    (float('nan'), 5, '+'),
    (10, float('nan'), '-'),
    (float('nan'), float('nan'), '*'),
])
def test_calculator_with_nan(a, b, operation):
    """Test calculator function with NaN values."""
    assert str(calculator(a, b, operation)) == "nan" or calculator(a, b, operation) != calculator(a, b, operation)