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
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, ):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)


sähköauta = Sähköauto('ABC-15', 180, 52.5 )
polttoauto = Polttomoottoriauto('ACD-123', 165, 32.3)

sähköauta.kiihdyta(180)
polttoauto.kiihdyta(165)

sähköauta.kulje(3)
polttoauto.kulje(3)

print(sähköauta.kuljettu)

print(polttoauto.kuljettu)