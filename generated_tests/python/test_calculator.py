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
    (-10, -5, '+', -15),
    (-10, 5, '-', -15),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Test normal and edge cases for the calculator function.
    """
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ('a', 5, '+'),
    (10, 'b', '-'),
    (None, 5, '*'),
    (10, None, '/'),
])
def test_calculator_with_invalid_inputs(a, b, operation):
    """
    Test the calculator function with invalid types to ensure it doesn't break.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

@pytest.mark.parametrize("a, b, expected_error_message", [
    (10, 0, "Error: Division by zero is not allowed."),
    (10, 5, "Error: Invalid operation."),
])
def test_calculator_failure_scenarios(a, b, expected_error_message):
    """
    Test failure scenarios for the calculator function.
    """
    for operation in ['/', '%']:
        assert calculator(a, b, operation) == expected_error_message