class Coffee:
    def __init__(self, coffee_type, size):
        self.coffee_type = coffee_type
        self.size = size

    def brew(self):
        return f"Brewing a {self.size} {self.coffee_type} coffee."

    def display_details(self):
        return f"Coffee Type: {self.coffee_type}, Size: {self.size}"