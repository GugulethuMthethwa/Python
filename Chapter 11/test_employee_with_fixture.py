import pytest
from employee import Employee

@pytest.fixture
def sample_employee():
    """Fixture to create a sample employee instance."""
    return Employee("Sam", "Johnson", 40000)

def test_give_default_raise(sample_employee):
    """Test giving the default raise of $5000."""
    sample_employee.give_raise()
    assert sample_employee.annual_salary == 45000

def test_give_custom_raise(sample_employee):
    """Test giving a custom raise amount."""
    sample_employee.give_raise(8000)
    assert sample_employee.annual_salary == 48000