class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.maxspeed = max_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Auton rekisteri numero on: {self.register_number}"
        f", jonka huippunopeus on {self.maxspeed} km/h"
        f", jonka matkamittari on {self.odometer} km"
        f", jonka tämänhetkinen nopeus on {self.speed} km/h.")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.maxspeed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        elif self.speed + speed_change >= 150:
            self.speed = 150
        # TODO: jos uusi nopeus > maksimi: nopeus = maksimi

someCar = Car("ABC-123", 120)
otherCar = Car("DEF-456", 150)
otherCar.accelerate(2330)
otherCar.accelerate(15)
otherCar.print_info()
otherCar.accelerate(-200)
otherCar.print_info()

