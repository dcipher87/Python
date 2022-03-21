# ### 11.1 City Country

# import unittest
# from city_functions import city_country 

# class CityCountryTestCase(unittest.TestCase):
#     """Test for city_functions.py"""
#     def test_city_country(self):
#         """Do city/country pairs like 'Cairo Egypt' work?"""
#         city_and_country = city_country("cairo", "egypt")
#         self.assertEqual(city_and_country, "Cairo Egypt")

#     def test_city_country_population(self):
#         """Does info like 'Cairo Egypt - population 500k work?"""
#         city_and_country = city_country("cairo", "egypt", 5439087)
#         self.assertEqual(city_and_country, "Cairo Egypt -5439087")

# if __name__ == '__main__':
#     unittest.main()

# ### 11.3 Employee
# import unittest

# class Employee:
#     """Provides employee names and salary."""

#     def __init__(self, first, last, salary):
#         """Initialise first, last name and salary attributes."""
#         self.first_name = first
#         self.last_name = last
#         self.salary = salary

#     def give_raise(self, salary=5000):
#         """Increase salary by amount provided or 5000."""
#         self.salary += salary

# class TestEmployee(unittest.TestCase):
#     """Test for the Employee class."""

#     def setUp(self):
#         """Create an employee with first, last names and salary."""
#         self.my_employee = Employee("James", "Blunt", 90000)

#     def test_give_raise_default(self):
#         """Test method to increase salary by 5000 default."""
#         self.my_employee.give_raise()
#         self.assertEqual(self.my_employee.salary, 90000 + 5000)

#     def test_give_raise_custom(self):
#         """Test method to increase salary by custom amount(8500)"""
#         self.my_employee.give_raise(8500)
#         self.assertEqual(self.my_employee.salary, 90000 + 8500)





