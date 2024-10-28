class Player:
    """A class representing a dodgeball player"""
    def __init__(self, name, number, position) -> None:
        self.name = name
        self.number = number
        self.position = position

    def get_position(self):
        """ A getter for position"""
        return self.position

    def get_name(self):
        """ A getter for name"""
        return self.name

    def get_number(self):
        """ A getter for number"""
        return self.number
