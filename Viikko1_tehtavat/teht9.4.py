# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random

class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.maxspeed = max_speed
        self.odometer = 0
        self.speed = 0
        self.travel_hours = 0

    def print_info(self):
        print(f"Car register number is: {self.register_number}"
              f", which topspeed is: {self.maxspeed} km/h"
              f", which current speed is: {self.speed} km/h"
              f", which total travelled distance is: {self.odometer} km"
              f", which total time it took to get distance travelled to 10 000km was: {self.travel_hours}")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.maxspeed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        else:
            self.speed = self.maxspeed

    def print_currentspeed(self):
        print(f"The speed of the car is {self.speed} km/h.")

    def travel_distance(self, hours):
        self.odometer = self.odometer + (self.speed * hours)
        self.travel_hours = self.travel_hours + hours

def car_make():
    cars = []
    for x in range(11):
        cars.append(Car("ABC-" + str(x), random.randint(100, 200)))
    return cars

cars = car_make()
race_total_distance = 10000

for car in cars:
    while car.odometer < race_total_distance:
        random_speed = random.randint(-10,15)
        Car.accelerate(car,random_speed)
        Car.travel_distance(car,1)
        if car.odometer >= race_total_distance:
            Car.print_info(car)


