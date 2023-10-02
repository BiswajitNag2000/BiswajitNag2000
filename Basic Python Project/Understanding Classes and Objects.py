class Vehicle:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


class Bus(Vehicle):
    pass


bus = Bus("Volvo",'B11R' ,'Red')
print("Vehicle Brand:", bus.brand, "Model:", bus.model, "Color:", bus.color)        