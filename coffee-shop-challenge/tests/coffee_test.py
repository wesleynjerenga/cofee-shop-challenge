import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.coffee = Coffee(type="Espresso", size="Medium")

    def test_coffee_type(self):
        self.assertEqual(self.coffee.type, "Espresso")

    def test_coffee_size(self):
        self.assertEqual(self.coffee.size, "Medium")

    def test_brew_coffee(self):
        self.assertEqual(self.coffee.brew(), "Brewing a Medium Espresso")

    def test_display_coffee_details(self):
        self.assertEqual(self.coffee.display_details(), "Coffee Type: Espresso, Size: Medium")

if __name__ == '__main__':
    unittest.main()