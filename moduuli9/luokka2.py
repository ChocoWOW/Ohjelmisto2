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


auto = Auto('rekisteritunnus ABC-123', 142)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f'auton nopeus: {auto.nopeusnyt} km/h')
print('Jarrutus!')
auto.kiihdyta(-200)
print(f'auton nopeus: {auto.nopeusnyt} km/h\n')
print(f'{auto.rekistiretunnus}\nauton huppunopeus on: {auto.huippunopeus}\nnopeus on: {auto.nopeusnyt} km/h \nkuljettu: {auto.kuljettu} km')