class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.hissi = alin_kerros
        self.alin = alin_kerros
        self.ylin = ylin_kerros
    def kerros_alas(self):
        print(f'hissi on kerroksessa: {self.hissi}')
        self.hissi = self.hissi - 1

    def kerros_ylos(self):
        print(f'hissi on kerroksessa: {self.hissi}')
        self.hissi = self.hissi + 1
    def siirry_kerrokseen(self, kohde):
        while kohde != self.hissi:
            if kohde < self.hissi:
                self.kerros_alas()
            if kohde > self.hissi:
                self.kerros_ylos()
        print(f'hissi on kerroksessa: {self.hissi}')
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.maara = hissien_maara
        self.hissit = []
        while len(self.hissit) <= hissien_maara:
            self.hissit.append(Hissi(self.alin, self.ylin))
    def aja_hissiä(self, hissi, kohde):
        self.hissi = self.hissit[hissi]
        self.hissit[hissi].siirry_kerrokseen(kohde)
    def palohalytys(self):
        print('Varoitus tulipalo!')
        i = 0
        while i < len(self.hissit):
            self.aja_hissiä(i,self.alin)
            i += 1

talo = Talo(1, 5, 10)

talo.aja_hissiä(0,5)

talo.palohalytys()
