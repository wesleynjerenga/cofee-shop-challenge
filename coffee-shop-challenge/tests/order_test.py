import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(name="John Doe", email="john@example.com")
        self.coffee = Coffee(type="Espresso", size="Medium")
        self.order = Order(order_id=1, customer=self.customer, coffee=self.coffee)

    def test_order_creation(self):
        self.assertEqual(self.order.order_id, 1)
        self.assertEqual(self.order.customer.name, "John Doe")
        self.assertEqual(self.order.coffee.type, "Espresso")

    def test_calculate_total(self):
        self.order.coffee.price = 3.50  # Assuming Coffee class has a price attribute
        self.assertEqual(self.order.calculate_total(), 3.50)

    def test_order_status(self):
        self.order.status = "Pending"
        self.assertEqual(self.order.status, "Pending")
        self.order.status = "Completed"
        self.assertEqual(self.order.status, "Completed")

if __name__ == '__main__':
    unittest.main()