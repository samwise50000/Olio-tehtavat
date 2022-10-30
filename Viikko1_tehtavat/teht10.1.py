# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

import random

class Hissi:
    def __init__(self, lowest_floor, highest_floor):
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.current_floor = 1


    def siirry_kerrokseen(self, haluttu_kerros):
        if self.current_floor < haluttu_kerros:
            for x in range(self.current_floor, haluttu_kerros):
                self.kerros_ylos()
        else:
            for x in range(haluttu_kerros, self.current_floor):
                self.kerros_alas()

    def kerros_ylos(self):
        self.current_floor += 1
        print(self.current_floor)

    def kerros_alas(self):
        self.current_floor -= 1
        print(self.current_floor)

hissi = Hissi(1, 6)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)
