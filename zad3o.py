class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House: {self.area} m^2, rooms: {self.rooms}, price: {self.price} zł, "
                f"address: {self.address}, plot: {self.plot} m^2")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat: {self.area} m^2, rooms: {self.rooms}, price: {self.price} zł, "
                f"address: {self.address}, floor: {self.floor}")


house1 = House(120, 5, 850000, 'Kraków, Lipowa 10', 300)
flat1 = Flat(55,2, 420000, 'Warszawa, Jana Pawła II 3', 7)

print(house1)
print(flat1)

