# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.maxspeed = max_speed
        self.odometer = 2000
        self.speed = 0

    def print_info(self):
        print(f"Car register number is: {self.register_number}"
              f", which topspeed is: {self.maxspeed} km/h"
              f", which current speed is: {self.speed} km/h"
              f", which total travelled distance is: {self.odometer} km.")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.maxspeed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        elif self.speed + speed_change >= 142:
            self.speed = 142

    def print_currentspeed(self):
        print(f"The speed of the car is {self.speed} km/h.")

    def travel_distance(self, time):
        self.odometer = self.odometer + self.speed * time

    def print_travel_distance(self):
        print(f"The total amount of travelled is {int(self.odometer)} km.")

someCar = Car("ABC-123", 142)
someCar.accelerate(60)
someCar.travel_distance(1.5)
someCar.print_travel_distance()