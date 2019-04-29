class auto():
    def __init__(self, minute, capacity, pomp, time):
        self.minute = minute
        self.capacity = capacity
        self.tank = 0
        self.pomp = pomp
        self.time = time
        self.czas = ['X']
        self.wait = 0
    def tankowanie(self):
        self.tank+=1000
        self.wait+=1
        self.czas.append('O')
        if self.capacity == self.tank:
            self.wait = 0
            return 1
    def zrzut(self):
        self.tank-=2000
        self.czas.append('X')
        if self.tank == 0:
            return 1
    def jazda(self):
        self.wait+=1
        if self.wait<=3:
            self.czas.append('-')
        else:
            self.wait = 0
            return 1
    def czekanie(self):
        self.czas.append('||')
    def do(self, minuta):
        if self.minute <= minuta:
            if self.czas[-1] == 'X':
                self.jazda()
            elif self.czas[-1] == '-' and self.wait != 0:
                self.jazda()
            elif self.czas[-1] == '-' and self.wait == 0 and self.tank == 0:
                self.tankowanie()
            elif self.czas[-1] == '-' and self.wait == 0 and self.tank == 2000:
                self.zrzut()
            elif self.czas[-1] == 'O' and self.wait !=0:
                self.tankowanie()
            elif self.czas[-1] == 'O' and self.wait == 0:
                self.jazda()
            else:
                self.czekanie()
A1 = auto(5, 2000, 2000, 3)
for i in range(35):
    #print('krok ', i)
    A1.do(i)
print(A1.czas)
