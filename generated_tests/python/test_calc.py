import pytest
from unittest.mock import patch
from calc import main

@pytest.fixture
def mock_inputs():
    """Fixture to mock input values."""
    with patch('builtins.input', side_effect=["2", "3"]):
        yield

@pytest.fixture
def mock_inputs_zero_division():
    """Fixture to mock input for zero division case."""
    with patch('builtins.input', side_effect=["4", "0"]):
        yield

@pytest.fixture
def mock_inputs_negative():
    """Fixture to mock input for negative numbers."""
    with patch('builtins.input', side_effect=["-5", "-10"]):
        yield

@pytest.fixture
def mock_print(mocker):
    """Fixture to mock print function."""
    mocker.patch('builtins.print')

def test_main_normal_case(mock_inputs, mock_print):
    """Test main function with normal positive numbers."""
    main()
    mock_print.assert_any_call("The sum is: 5.0")
    mock_print.assert_any_call("The difference is: -1.0")
    mock_print.assert_any_call("The product is: 6.0")
    mock_print.assert_any_call("The quotient is: 0.6666666666666666")

def test_main_zero_division_case(mock_inputs_zero_division, mock_print):
    """Test main function handling division by zero."""
    main()
    mock_print.assert_any_call("The sum is: 4.0")
    mock_print.assert_any_call("The difference is: 4.0")
    mock_print.assert_any_call("The product is: 0.0")
    mock_print.assert_any_call("The quotient is: undefined (division by zero)")

def test_main_negative_numbers_case(mock_inputs_negative, mock_print):
    """Test main function with negative numbers."""
    main()
    mock_print.assert_any_call("The sum is: -15.0")
    mock_print.assert_any_call("The difference is: 5.0")
    mock_print.assert_any_call("The product is: 50.0")
    mock_print.assert_any_call("The quotient is: 0.5")

def test_main_with_invalid_input(mocker):
    """Test main function with invalid input, expecting ValueError."""
    mocker.patch('builtins.input', side_effect=["not a number", "3"])

    with pytest.raises(ValueError):
        main()