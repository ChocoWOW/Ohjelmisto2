
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
kilpailijat = []
i = 0
while i != 10:
    i += 1
    nopeus = random.randint(100,200)
    kilpailijat.append(Auto(f'abc-{i}', nopeus))
b = 0
while True:
    wee = random.randint(-10,15)
    kilpailijat[b].kiihdyta(wee)
    kilpailijat[b].kulje(1)
    if kilpailijat[b].kuljettu >= 10000:
        break
    if b < 9:

        b += 1
    else:
        b = 0
for i in range(len(kilpailijat)):
    print(f'nimi: {kilpailijat[i].rekisteritunnus} \nhuippu nopeus: {kilpailijat[i].huippunopeus}'
          f' \nnopeus lopussa: {kilpailijat[i].nopeusnyt} \nkuljettu: {kilpailijat[i].kuljettu}\n\n')