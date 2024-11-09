import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, '+', 15),  # normal case for addition
    (10, 5, '-', 5),   # normal case for subtraction
    (10, 5, '*', 50),  # normal case for multiplication
    (10, 2, '/', 5),   # normal case for division
    (10, 0, '/', "Error: Division by zero is not allowed."),  # division by zero
    (10, 5, '%', "Error: Invalid operation."),  # invalid operation
    (0, 0, '+', 0),    # edge case: adding zeros
    (-5, -5, '+', -10),  # edge case: adding negatives
    (-5, 5, '*', -25),  # edge case: negative times positive
])
def test_calculator_normal_and_edge_cases(a, b, operation, expected):
    """Test calculator function with normal, edge, and error cases."""
    assert calculator(a, b, operation) == expected

@pytest.mark.parametrize("a, b, operation", [
    ('a', 5, '+'),  # non-numeric input for a
    (10, 'b', '-'),  # non-numeric input for b
    (None, 5, '*'),  # None as input for a
    (10, None, '/'),  # None as input for b
])
def test_calculator_with_invalid_inputs(a, b, operation):
    """Test calculator function with invalid inputs expecting exceptions."""
    with pytest.raises(TypeError):
        calculator(a, b, operation)

def test_calculator_division_by_zero_mocked():
    """Test division by zero using mocking to handle unexpected changes."""
    with pytest.raises(ZeroDivisionError):
        calculator(10, 0, '/')

# If there were any external dependencies like a database or API call,
# here would be the place to use mocks or patches to simulate those interactions
# in a controlled way, ensuring the unit tests remain focused on the calculator functionality.