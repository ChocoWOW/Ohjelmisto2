class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekistiretunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = 0
        self.kuljettu = 0
auto = Auto('rekisteritunnus ABC-123', 'huippunopeus 142 km/h')

print(f'{auto.rekistiretunnus}\n{auto.huippunopeus}\n{auto.nopeusnyt}\n{auto.kuljettu}')