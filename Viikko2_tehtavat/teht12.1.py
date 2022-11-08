# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests

get_joke = "https://api.chucknorris.io/jokes/random"

try:
    joke = requests.get(get_joke).json()
    print(joke["value"])
except:
    print("Error, no internet connection?")