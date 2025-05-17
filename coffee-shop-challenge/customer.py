class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_info(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email

    def get_info(self):
        return {
            "name": self.name,
            "email": self.email
        }