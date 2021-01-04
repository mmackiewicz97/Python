class SavetoFile:
    def __init__(self, path):
        self.path= path
        with open(self.path, "a") as f:
            f.write("save to path\n")

class Write10000:
    def __init__(self, path):
        self.path= path
        with open(self.path, "a") as f:
            f.write("10000\n")

class Sum:
    def __init__(self, path):
        self.path= path
        self.sum = 0
        with open(self.path, "r") as f:
            for i in f.readlines():
                if i == "10000\n":
                    self.sum += 10000
        with open(self.path, "a") as f:
            f.write(f'sum:{self.sum}\n')

class KomendaA:
    def __init__(self, path, godzina, minuta):
        self.path = path
        f = open(self.path, "r")
        self.godzina = godzina
        self.minuta = minuta
        SavetoFile(self.path)
        f.close()
class KomendaB:
    def __init__(self, path, godzina, minuta):
        self.path = path
        f = open(self.path, "r")
        self.godzina = godzina
        self.minuta = minuta
        Write10000(self.path)
        f.close()
class KomendaC:
    def __init__(self, path, godzina, minuta):
        self.path = path
        f = open(self.path, "r")
        self.godzina = godzina
        self.minuta = minuta
        Sum(self.path)
        f.close()
if __name__=="__main__":
    system_timehh = 0
    system_timemm = 0
    for i in range(24*60):
        system_timemm += 1
        if i % 60 == 0:
            system_timehh += 1
        KomendaA("plik", system_timehh, system_timemm)
        KomendaA("plik", system_timehh, system_timemm)
        KomendaB("plik", system_timehh, system_timemm)
        KomendaB("plik", system_timehh, system_timemm)
        KomendaC("plik", system_timehh, system_timemm)
        KomendaC("plik", system_timehh, system_timemm)
