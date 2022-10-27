class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.maxspeed = max_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Auton rekisteri numero on: {self.register_number}")
        print(f"Huippunopeus on: {self.maxspeed} km/h.")
        print(f"Matkamittari: {self.odometer} km.")
        print(f"Tämänhetkinen nopeus on: {self.speed} km/h.")

    def accelerate(self):
        self.speed = self.speed + 3

someCar = Car("ABC-123", 120)
otherCar = Car("DEF-456", 150)
otherCar.accelerate()
otherCar.accelerate()
someCar.print_info()
otherCar.print_info()

