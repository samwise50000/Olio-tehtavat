# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.nykyinen_kerros = 1


    def siirry_kerrokseen(self, haluttu_kerros):
        if self.nykyinen_kerros < haluttu_kerros:
            for x in range(self.nykyinen_kerros, haluttu_kerros):
               if self.nykyinen_kerros < self.ylin_kerros:
                   self.kerros_ylos()

        else:
            for x in range(haluttu_kerros, self.nykyinen_kerros):
                if self.nykyinen_kerros > self.alin_kerros:
                    self.kerros_alas()

    def kerros_ylos(self):
        self.nykyinen_kerros += 1
        print(self.nykyinen_kerros)

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(self.nykyinen_kerros)

hissi = Hissi(1, 6)
hissi.siirry_kerrokseen(3)
hissi.siirry_kerrokseen(3)
