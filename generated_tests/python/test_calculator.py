import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

# Test suite for the calculator function in calculator.py

@pytest.fixture
def setup():
    # Setup if needed
    pass

@pytest.fixture
def teardown():
    # Teardown if needed
    pass

# Testing Addition
@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, '+', 8),
    (-1, -1, '+', -2),
    (0, 0, '+', 0),
    (1.5, 2.5, '+', 4.0),
])
def test_calculator_addition(a, b, operation, expected, setup, teardown):
    """Test the addition operation."""
    assert calculator(a, b, operation) == expected

# Testing Subtraction
@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, '-', 2),
    (-1, 1, '-', -2),
    (0, 0, '-', 0),
    (2.5, 1.5, '-', 1.0),
])
def test_calculator_subtraction(a, b, operation, expected, setup, teardown):
    """Test the subtraction operation."""
    assert calculator(a, b, operation) == expected

# Testing Multiplication
@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, '*', 15),
    (-1, -1, '*', 1),
    (0, 5, '*', 0),
    (1.5, 2, '*', 3.0),
])
def test_calculator_multiplication(a, b, operation, expected, setup, teardown):
    """Test the multiplication operation."""
    assert calculator(a, b, operation) == expected

# Testing Division
@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 2, '/', 2.5),
    (-1, -1, '/', 1),
    (5, 0, '/', "Error: Division by zero is not allowed."),
    (1.5, 0.5, '/', 3.0),
])
def test_calculator_division(a, b, operation, expected, setup, teardown):
    """Test the division operation."""
    assert calculator(a, b, operation) == expected

# Testing Invalid Operation
@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, 'x', "Error: Invalid operation."),
    (5, 3, '%', "Error: Invalid operation."),
])
def test_calculator_invalid_operation(a, b, operation, expected, setup, teardown):
    """Test handling of invalid operation inputs."""
    assert calculator(a, b, operation) == expected

# Testing Edge Cases
@pytest.mark.parametrize("a, b, operation, expected", [
    ('a', 3, '+', "Error: Invalid inputs."),  # Assuming handling of non-numeric inputs
    (5, 'b', '-', "Error: Invalid inputs."),  # Assuming handling of non-numeric inputs
    ([], {}, '*', "Error: Invalid inputs."),  # Assuming handling of non-numeric inputs
])
def test_calculator_edge_cases(a, b, operation, expected, setup, teardown):
    """Test handling of edge cases."""
    with pytest.raises(TypeError):  # Assuming calculator function raises TypeError for invalid input types
        calculator(a, b, operation)