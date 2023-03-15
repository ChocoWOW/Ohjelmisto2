
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeusnyt = 0, kuljettu = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = nopeusnyt
        self.kuljettu = kuljettu
    def kiihdyta(self, muutos):
        self.nopeusnyt +=muutos
        if self.nopeusnyt > self.huippunopeus:
            self.nopeusnyt = self.huippunopeus
        if self.nopeusnyt < 0:
            self.nopeusnyt = 0
    def kulje(self, tunti):
        self.kuljettu += tunti * self.nopeusnyt
class Kilpailu:
    def __init__(self, nimet, pituus, kilpailijat = []):
        self.nimi = nimet
        self.pituus = pituus
        self.kilpailijat = kilpailijat
        i = 0
        while len(self.kilpailijat) < 10:
            nopeus1 = random.randint(100, 200)
            i += 1
            self.kilpailijat.append(Auto(f'abc-{i}', nopeus1))
    def tunti_kuluu(self):
        nopeus = random.randint(-10, 15)
        for i in range(len(self.kilpailijat)):
            self.kilpailijat[i].kiihdyta(nopeus)
            self.kilpailijat[i].kulje(1)
    def tulosta_tilanne(self):
        for i in range(len(self.kilpailijat)):
            print(f'Tunnus: {self.kilpailijat[i].rekisteritunnus}\n'
                  f'Nopeus nyt:{self.kilpailijat[i].nopeusnyt}\n'
                  f'Matka kuljettu: {self.kilpailijat[i].kuljettu}\n'
                  f'Maksimi nopeus: {self.kilpailijat[i].huippunopeus}\n')
    def kilpailu_ohi(self):
        for i in range(len(self.kilpailijat)):
            if self.kilpailijat[i].kuljettu > 8000:
                return True
            else:
                return False
kilpailu = []
kisa = Kilpailu('Suuri romuralli', 8000, kilpailu)

while kisa.kilpailu_ohi() == False:
    kulunut = 0
    kisa.tunti_kuluu()
    if kisa.kilpailu_ohi() == True:
        break
    kulunut += 1
    if kulunut % 10 == 1:
        print(kisa.tulosta_tilanne())

print(kisa.tulosta_tilanne())