import pytest
from employee import Employee

def test_give_default_raise():
    """Test giving the default raise of $5000."""
    employee = Employee("John", "Doe", 50000)
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise():
    """Test giving a custom raise amount."""
    employee = Employee("Jane", "Smith", 60000)
    employee.give_raise(10000)
    assert employee.annual_salary == 70000