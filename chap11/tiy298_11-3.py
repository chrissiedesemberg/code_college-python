class Employee():
    """Collect and update employee information"""

    def __init__(self, first_name, last_name, salary):
        """Collect information about employee"""
        self.first = first_name
        self.last = last_name
        self.salary = salary

    def pay_more(self, amount=5000):
        """Give employee a raise"""
        self.salary += amount

import unittest
# from chap11.tiy298_11-3 Employee

class TestSalaryIncrease(unittest.TestCase):
    """Test if class works"""
        
    def setUp(self):
        """Create test case where we test to see if raise class works"""
        self.employee_1 = Employee("William", "Shakespeare", 15000)

    def test_give_default_raise(self):
        self.employee_1.pay_more()
        self.assertEqual(self.employee_1.salary, 20000)

    def test_give_custom_raise(self):
        self.employee_1.pay_more(10000)
        self.assertEqual(self.employee_1.salary, 25000)

if __name__ == "__main__":
    unittest.main()