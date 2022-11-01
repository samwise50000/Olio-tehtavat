class Vehicle:
    def __init__(self):
        self.speed = 0
        self.odometer = 0

    def accelerate(self):
        self.speed += 1

    def print_info(self):
        print(f"V1 speed: {self.speed}, odometer: {self.odometer}")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.gas_level = 30

v1 = Car()
v1.accelerate()
v1.print_info()