class Konta:
    def __init__(self, stan, debet, max_przekroczenie):
        self.stan = stan
        self.debet = debet
        self.max_przekroczenie = max_przekroczenie
    def wyplac(self, kwota):
        if self.czy_przekroczony_debet():
            raise Exception("Przekroczono debet!")
        else:
            if abs(self.stan) + self.debet + self.max_przekroczenie < kwota:
                raise Exception("Za duża kwota!")
            else:
                self.stan -= kwota
                return True

    def czy_przekroczony_debet(self):
        if self.stan < 0:
            if abs(self.stan) > self.debet:
                return True
        else:
            return False

class zwykleKonto(Konta):
    def __init__(self, stan, debet):
        super(zwykleKonto, self).__init__(stan, debet, 100)

class VIPKonto(Konta):
    def __init__(self, stan, debet):
        super(VIPKonto, self).__init__(stan, debet, 1000)

    def wyplac(self, kwota):
        if self.stan > 0:
            self.max_przekroczenie = 2000
        else:
            self.max_przekroczenie = 1000
        if self.czy_przekroczony_debet():
            raise Exception("Przekroczono debet!")
        else:
            if abs(self.stan) + self.debet + self.max_przekroczenie < kwota:
                raise Exception("Za duża kwota!")
            else:
                self.stan -= kwota
                return True

class firmoweKonto(Konta):
    def __init__(self, stan, debet):
        super(firmoweKonto, self).__init__(stan, debet, 2000)
    def wyplac(self, kwota):
        if self.czy_przekroczony_debet():
                raise Exception("Przekroczono debet!")
        else:
            if abs(self.stan) + self.debet + self.max_przekroczenie < kwota:
                raise Exception("Za duża kwota!")
            else:
                self.stan -= kwota
                return True