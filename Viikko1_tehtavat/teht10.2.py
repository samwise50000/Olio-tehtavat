# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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
        print(f"Nykyinen kerros on: {self.nykyinen_kerros}")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Nykinen kerros on: {self.nykyinen_kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_maara = hissien_maara

        self.hissit = []

        for x in range(hissien_maara):
            h = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(h)

    def aja_hissia(self, hissin_numero, hissin_kohdekerros):
        for x in range(self.hissien_maara):
            if x == hissin_numero:
                hissi = self.hissit[x]
                print(f"Liikutaan hissillä: {x}, kerroksesta {hissi.nykyinen_kerros}")
                hissi.siirry_kerrokseen(hissin_kohdekerros)
                print(f"Hissi {x} on nyt kerroksessa {hissin_kohdekerros}.")




talo = Talo(1, 5, 3)
talo.aja_hissia(0, 3)
talo.aja_hissia(1, 2)
talo.aja_hissia(2, 4)