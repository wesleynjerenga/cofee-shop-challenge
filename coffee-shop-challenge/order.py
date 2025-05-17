class Order:
    """Represents an order linking a customer, a coffee, and a price."""
    _all = []

    def __init__(self, customer, coffee, price):
        """
        Initialize an Order instance.

        Args:
            customer (Customer): The customer placing the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the order (1.0–10.0).
        """
        from customer import Customer
        from coffee import Coffee
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        if not isinstance(price, (float, int)):
            raise TypeError("price must be a float or int.")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0.")
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order._all.append(self)

    @property
    def customer(self):
        """Return the customer who placed the order."""
        return self._customer

    @property
    def coffee(self):
        """Return the coffee ordered."""
        return self._coffee

    @property
    def price(self):
        """Return the price of the order."""
        return self._price

    @classmethod
    def all(cls):
        """Return all Order instances."""
        return cls._all