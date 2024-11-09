import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, '+', 8),
    (10, 5, '-', 5),
    (4, 2, '*', 8),
    (8, 4, '/', 2),
    (10, 0, '/', "Error: Division by zero is not allowed."),
    (5, 2, '%', "Error: Invalid operation."),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Test normal and edge cases for calculator function.
    """
    assert calculator(a, b, operation) == expected, "Calculator did not return expected result."

@pytest.mark.parametrize("a, b, operation", [
    ('a', 2, '+'),
    (3, 'b', '-'),
    (None, 1, '*'),
    (1, None, '/'),
])
def test_calculator_input_errors(a, b, operation):
    """
    Test error cases for calculator with invalid inputs.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

def test_calculator_division_by_zero():
    """
    Test division by zero error case specifically.
    """
    result = calculator(5, 0, '/')
    assert result == "Error: Division by zero is not allowed.", "Calculator did not handle division by zero as expected."

def test_calculator_invalid_operation():
    """
    Test invalid operation error case specifically.
    """
    result = calculator(5, 5, 'invalid')
    assert result == "Error: Invalid operation.", "Calculator did not handle invalid operation as expected."