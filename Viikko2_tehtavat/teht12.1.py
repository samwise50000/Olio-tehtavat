# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests

get_joke = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(get_joke)
    if response.status_code == 200:
        joke = response.json()
        print(joke["value"])
    else:
        print("Check URL- address!")
except requests.exceptions.RequestException as e:
    print(f"Error, no internet connection? Error: {e}")