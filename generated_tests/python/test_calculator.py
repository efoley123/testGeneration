import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.fixture(scope="module")
def setup_teardown():
    """
    Setup resources before tests and teardown after all tests are done.
    """
    # Setup can be done here if needed
    yield
    # Teardown can be done here if needed

@pytest.mark.usefixtures("setup_teardown")
class TestCalculator:
    @pytest.mark.parametrize("a, b, operation, expected", [
        (1, 1, '+', 2),
        (-1, -1, '+', -2),
        (1.5, 2.5, '+', 4.0),
        (0, 0, '+', 0),
        (1000000, 2000000, '+', 3000000),
    ])
    def test_addition_normal_cases(self, a, b, operation, expected):
        """
        Test addition with normal cases including positive, negative, and large numbers.
        """
        assert calculator(a, b, operation) == expected

    @pytest.mark.parametrize("a, b, operation, expected", [
        (5, 3, '-', 2),
        (-5, -3, '-', -2),
        (2.5, 1.5, '-', 1.0),
        (0, 0, '-', 0),
        (1000000, 999999, '-', 1),
    ])
    def test_subtraction_normal_cases(self, a, b, operation, expected):
        """
        Test subtraction with normal cases including positive, negative, and large numbers.
        """
        assert calculator(a, b, operation) == expected

    @pytest.mark.parametrize("a, b, operation, expected", [
        (2, 3, '*', 6),
        (-2, -3, '*', 6),
        (2.5, 4, '*', 10.0),
        (0, 100, '*', 0),
        (1000, 2000, '*', 2000000),
    ])
    def test_multiplication_normal_cases(self, a, b, operation, expected):
        """
        Test multiplication with normal cases including positive, negative, and large numbers.
        """
        assert calculator(a, b, operation) == expected

    @pytest.mark.parametrize("a, b, operation, expected", [
        (6, 3, '/', 2),
        (-6, -3, '/', 2),
        (7.5, 2.5, '/', 3.0),
        (0, 5, '/', 0),
        (1000000, 2, '/', 500000.0),
    ])
    def test_division_normal_cases(self, a, b, operation, expected):
        """
        Test division with normal cases including positive, negative, and large numbers.
        """
        assert calculator(a, b, operation) == expected

    @pytest.mark.parametrize("a, b, operation, expected", [
        (1, 0, '/', "Error: Division by zero is not allowed."),
        (-1, 0, '/', "Error: Division by zero is not allowed."),
        (0, 0, '/', "Error: Division by zero is not allowed."),
    ])
    def test_division_by_zero(self, a, b, operation, expected):
        """
        Test division by zero scenarios to ensure appropriate error message is returned.
        """
        assert calculator(a, b, operation) == expected

    @pytest.mark.parametrize("a, b, operation, expected", [
        (1, 1, '^', "Error: Invalid operation."),
        (2, 2, 'invalid', "Error: Invalid operation."),
        (3, 3, '', "Error: Invalid operation."),
        (4, 4, None, "Error: Invalid operation."),
    ])
    def test_invalid_operation(self, a, b, operation, expected):
        """
        Test invalid operations to ensure appropriate error message is returned.
        """
        assert calculator(a, b, operation) == expected

    @pytest.mark.parametrize("a, b, operation", [
        ("a", 1, '+'),
        (1, "b", '-'),
        ("c", "d", '*'),
        (1, 0, '/'),
    ])
    def test_invalid_input_types(self, a, b, operation):
        """
        Test invalid input types to ensure TypeError is raised.
        """
        with pytest.raises(TypeError):
            calculator(a, b, operation)

    @pytest.mark.parametrize("a, b, operation, expected", [
        (1e308, 1e308, '+', float('inf')),
        (-1e308, -1e308, '+', float('-inf')),
        (1e308, 1e308, '*', float('inf')),
        (-1e308, 1e308, '*', float('-inf')),
    ])
    def test_large_number_operations(self, a, b, operation, expected):
        """
        Test operations with very large numbers to check for overflow.
        """
        assert calculator(a, b, operation) == expected

    def test_operation_case_sensitivity(self):
        """
        Test that operations are case-sensitive and invalid case returns error.
        """
        assert calculator(1, 1, '+') == 2
        assert calculator(1, 1, '+') == 2
        assert calculator(1, 1, 'PLUS') == "Error: Invalid operation."

    def test_none_operation(self):
        """
        Test that passing None as operation returns invalid operation error.
        """
        assert calculator(1, 1, None) == "Error: Invalid operation."