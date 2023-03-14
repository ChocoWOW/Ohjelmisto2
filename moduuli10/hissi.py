class Hissi:
    def __init__(self, alin_kerros, ylin):
        self.alin = alin_kerros
        self.ylin = ylin
    def kerros_alas(self):
        print(f'hissi on kerroksessa: {self.alin}')
        self.alin = self.alin - 1

    def kerros_ylos(self):
        print(f'hissi on kerroksessa: {self.alin}')
        self.alin = self.alin + 1
    def siirry_kerrokseen(self, kohde):
        while kohde != self.alin:
            if kohde < self.alin:
                self.kerros_alas()
            if kohde > self.alin:
                self.kerros_ylos()
        print(f'hissi on kerroksessa: {self.alin}')


h = Hissi(2, 10)
h.siirry_kerrokseen(8)
h.siirry_kerrokseen(3)

