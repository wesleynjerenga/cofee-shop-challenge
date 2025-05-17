import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(name="John Doe", email="john@example.com")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john@example.com")

    def test_customer_email_validation(self):
        invalid_customer = Customer(name="Jane Doe", email="invalid-email")
        self.assertFalse(invalid_customer.is_valid_email())

    def test_update_customer_info(self):
        self.customer.update_info(name="Jane Doe", email="jane@example.com")
        self.assertEqual(self.customer.name, "Jane Doe")
        self.assertEqual(self.customer.email, "jane@example.com")

if __name__ == '__main__':
    unittest.main()