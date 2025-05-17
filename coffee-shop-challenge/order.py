class Order:
    def __init__(self, order_id, customer, coffee):
        self.order_id = order_id
        self.customer = customer
        self.coffee = coffee
        self.status = 'Pending'

    def calculate_total(self):
        # Assuming coffee has a price attribute
        return self.coffee.price

    def process_order(self):
        # Logic to process the order
        self.status = 'Processed'

    def get_order_details(self):
        return {
            'order_id': self.order_id,
            'customer': self.customer.name,
            'coffee': self.coffee.type,
            'status': self.status
        }