class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f'{self.nimi}, Kirjoittaja: {self.kirjoittaja}. sivumäärä: {self.sivumäärä} sivua')

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f'{self.nimi}, Päätoimittaja: {self.päätoimittaja}')

julkaisut = []
julkaisut.append(Lehti('Aku Ankka', 'Aki Hyyppä'))
julkaisut.append(Kirja('Hytti n:o 6', 'Rosa Liksom', 200))

for t in julkaisut:
    t.tulosta_tiedot()