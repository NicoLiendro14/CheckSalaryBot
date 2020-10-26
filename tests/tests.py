import unittest
from unittest.mock import Mock, patch
import sys
sys.path.insert(1, '..')
import check_salary


@patch('check_salary.requests.get')
class TestCheckSalary(unittest.TestCase):
    def test_get_salary(self, mock_get):
        input_salary = "550000"
        output_salary = "115000"
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = output_salary
        response = check_salary.get_salary(input_salary)
        assert response.json() == output_salary




