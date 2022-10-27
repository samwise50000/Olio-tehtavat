# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.maxspeed = max_speed
        self.odometer = 0
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

someCar = Car("ABC-123", 142)
someCar.accelerate(30)
someCar.accelerate(70)
someCar.accelerate(50)
someCar.print_info()
print("Breaking -200 km/h")
someCar.accelerate(-200)
someCar.print_currentspeed()
