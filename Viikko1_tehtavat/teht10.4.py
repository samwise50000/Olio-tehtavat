# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
# Luokassa on seuraavat metodit:

# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

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
              f", which total travelled distance is: {self.odometer} km")

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

class Race:
    def __init__(self, race_name, race_distance, participants):
        self.race_name = race_name
        self.race_distance = race_distance
        self.participants = participants


    def hour_pass(self):
        for car in self.participants:
            car.accelerate(random.randint(-10, 15))
            car.travel_distance(1)

    def print_status(self):
        for car in self.participants:
            car.print_info()

    def race_over(self):
        for car in self.participants:
            if car.odometer >= self.race_distance:
                return True
        return False


def car_make():
    cars = []
    for x in range(10):
        cars.append(Car("ABC-" + str(x), random.randint(100, 200)))
    return cars

hour = 0
cars = car_make()
race = Race("The great junkrace", 8000, cars)
race.print_status()
while race.race_over() == False:
    race.hour_pass()
    hour += 1
    if hour % 10 == 0:
        print(f"{hour} hours has passed.")
        race.print_status()
print(f"The race has ended with total hours of {hour} hours! The results are:")
race.print_status()
for car in race.participants:
    if car.odometer >= race.race_distance:
        print(f"Car with the register number: {car.register_number}!")