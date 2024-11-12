import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from calculator import calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, '+', 15),
])
def test_calculator_(a, b, operation, expected):
    """Test calculator function with normal and edge cases."""
    assert calculator(a, b, operation) == expected