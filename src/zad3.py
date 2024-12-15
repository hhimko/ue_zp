class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"Property(area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address})"
        
class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f"House(area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address}, plot={self.plot})"
        
class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f"Flat(area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address}, floor={self.floor})" 
    
    
if __name__ == "__main__":
    h = House(106.2, 9, 750000, "Katowice ul. Bogucicka 44", 1000)
    f = Flat(40.7, 4, 240000, "Rybnik ul. Gliwicka 4B", 4)

    print(h)
    print(f)