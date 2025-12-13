import magazine.utils


class Order:
    def __init__(self, number):
        self.number = number

    def info(self):
        return f"Zamówienie #{self.number}, {magazine.utils.helper()}"