import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, '+', 8),
    (5, 3, '-', 2),
    (5, 3, '*', 15),
    (5, 3, '/', 5/3),
    (5, 0, '/', "Error: Division by zero is not allowed."),
    (5, 3, 'x', "Error: Invalid operation."),
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """
    Test normal and edge cases for calculator function. It checks if the operations
    are correctly performed or return the right error messages.
    """
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ('a', 3, '+'),
    (5, 'b', '-'),
    ('a', 'b', '*'),
])
def test_calculator_with_invalid_inputs(a, b, operation):
    """
    Test error cases for calculator function with invalid (non-numeric) inputs. It should
    not raise any errors but isn't expected to handle these inputs either, as the function
    definition does not include error handling for non-numeric inputs.
    """
    with pytest.raises(TypeError):
        calculator(a, b, operation)

def test_calculator_division_by_zero():
    """
    Specifically testing division by zero scenario to ensure the error message
    is returned as expected.
    """
    assert calculator(5, 0, '/') == "Error: Division by zero is not allowed."

def test_calculator_invalid_operation():
    """
    Testing invalid operation scenario to ensure the error message
    is returned as expected.
    """
    assert calculator(5, 5, 'invalid') == "Error: Invalid operation."