class food:
    def __init__(self, flavour, smell, colour, expiration_date):
        self.flavour = flavour
        self.smell = smell
        self.colour = colour
        self.expiration_date = expiration_date
    def edible(self):
        pass
    def tasty(self):
        pass

cake = food("sweet", "creamy", "mostly white", "7.30.2023")
