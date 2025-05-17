class Customer:
    _all = []

    def __init__(self, name):
        self.name = name
        Customer._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1–15 characters.")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        spending = {}
        for order in Order._all:
            if order.coffee is coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price
        if not spending:
            return None
        return max(spending, key=spending.get)