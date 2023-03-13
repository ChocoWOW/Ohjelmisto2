import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeusnyt = 0, kuljettu = 0):
        self.rekistiretunnus = rekisteritunnus
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


auto = Auto('rekisteritunnus ABC-123', 142)
auto.kiihdyta(200)
print(f'nopeus on: {auto.nopeusnyt} km/h \nkuljettu: {auto.kuljettu} km')
auto.kulje(1)
print(f'nopeus on: {auto.nopeusnyt} km/h \nkuljettu: {auto.kuljettu} km')