import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, '+', 15),
    (10, 5, '-', 5),
    (10, 5, '*', 50),
    (10, 2, '/', 5),
    (10, 0, '/', "Error: Division by zero is not allowed."),
    (1, 1, 'invalid', "Error: Invalid operation."),
    (0, 0, '+', 0),
    (-1, -1, '*', 1),
    (-10, 5, '/', -2),
    (10, -5, '-', 15),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Tests calculator with normal and edge cases, including error messages for division by zero and invalid operations.
    """
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ('a', 5, '+'),
    (10, 'b', '-'),
    ('a', 'b', '*'),
])
def test_calculator_with_non_numeric_inputs(a, b, operation):
    """
    Tests calculator with non-numeric inputs to ensure it raises an appropriate TypeError.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

def test_division_by_zero():
    """
    Tests specifically the division operation to ensure it handles division by zero correctly.
    """
    assert calculator(10, 0, '/') == "Error: Division by zero is not allowed."

def test_invalid_operation():
    """
    Tests calculator with an invalid operation to ensure it returns the correct error message.
    """
    assert calculator(10, 5, 'invalid_operation') == "Error: Invalid operation."