import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

# Test cases for the calculator function to ensure comprehensive coverage

@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, '+', 8),
    (10, 5, '-', 5),
    (2, 4, '*', 8),
    (10, 2, '/', 5),
    (10, 0, '/', "Error: Division by zero is not allowed."),
    (1, 1, 'invalid_op', "Error: Invalid operation."),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Test normal and edge cases for the calculator function.
    Covers all basic operations and checks for division by zero and invalid operations.
    """
    assert calculator(a, b, operation) == expected, "The calculator did not return the expected result."

@pytest.mark.parametrize("a, b, operation", [
    ('a', 5, '+'),
    (2, 'b', '-'),
    ('a', 'b', '*'),
])
def test_calculator_with_non_numeric_inputs(a, b, operation):
    """
    Test the calculator function with non-numeric inputs.
    Expecting it to raise a TypeError.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

@pytest.mark.parametrize("a, b, operation", [
    (None, 5, '+'),
    (2, None, '-'),
    (None, None, '*'),
])
def test_calculator_with_none_inputs(a, b, operation):
    """
    Test the calculator function with None as inputs.
    Expecting it to raise a TypeError.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

# Test division by zero using mocks to simulate the situation
@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 0, '/', "Error: Division by zero is not allowed."),
])
def test_calculator_division_by_zero(a, b, operation, expected):
    """
    Test division by zero specifically to ensure the function handles it gracefully.
    """
    assert calculator(a, b, operation) == expected, "The calculator did not handle division by zero as expected."

# Test invalid operation handling
@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 2, 'x', "Error: Invalid operation."),
])
def test_calculator_invalid_operation(a, b, operation, expected):
    """
    Test how the calculator handles invalid operations.
    """
    assert calculator(a, b, operation) == expected, "The calculator did not handle the invalid operation as expected."