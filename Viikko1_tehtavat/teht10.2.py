# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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
