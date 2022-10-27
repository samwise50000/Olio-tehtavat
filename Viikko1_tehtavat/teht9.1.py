# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.maxspeed = max_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Car register number is: {self.register_number}")
        print(f"The topspeed of the car is: {self.maxspeed} km/h.")
        print(f"The current speed of the car is: {self.speed} km/h.")
        print(f"The total travelled distance is: {self.odometer} km.")


    def accelerate(self):
        self.speed = self.speed + 3

someCar = Car("ABC-123", 142)

someCar.print_info()
