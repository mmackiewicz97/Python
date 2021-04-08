import random
import numpy
import matplotlib.pyplot as plt


class ChromosomA:
    def __init__(self):
        self.geny = []

    def dodaj_gen(self, gen):
        self.geny.append(gen)

    def sumuj_geny(self):
        sum_p = 0
        sum_n = 0
        for i in range(0, len(self.geny), 2):
            sum_p += self.geny[i]
        for i in range(1, len(self.geny), 2):
            sum_n += self.geny[i]
        return sum_p, sum_n


class OsobaA:
    def __init__(self):
        self.chromosomy = self.stworz_chromosomy(1)

    def stworz_chromosomy(self, liczba_chromosomow):
        chromosomy = []
        for i in range(liczba_chromosomow):
            chr = ChromosomA()
            for j in range(50):
                chr.dodaj_gen(random.randint(10, 99))
            chromosomy.append(chr)
        return chromosomy

    def ocen(self):
        sum_p = 0
        sum_n = 0
        for i in self.chromosomy:
            p, n = i.sumuj_geny()
            sum_p += p
            sum_n += n
        return sum_p, 50*(99-10)-sum_n


class ChromosomB:
    def __init__(self):
        self.geny = []

    def dodaj_gen(self, gen):
        self.geny.append(gen)

    def sprawdz_atrakcyjnosc(self):
        sum = self.geny[5] + self.geny[45]
        for x in self.geny[80:111]:
            sum += 0.5 * x
        return sum/(2*(99-10)+31*(99-10)*0.5)

    def sprawdz_odpornosc(self):
        sum = 0
        for x in self.geny[56:77]:
            sum += x
        for x in self.geny[100:140]:
            sum += x
        return sum/((21+40)*(99-10))


class OsobaB:
    def __init__(self):
        self.chromosomy = self.stworz_chromosomy(2)

    def stworz_chromosomy(self, liczba_chromosomow):
        chromosomy = []
        for i in range(liczba_chromosomow):
            chr = ChromosomB()
            for j in range(148):
                chr.dodaj_gen(random.randint(10, 99))
            chromosomy.append(chr)
        return chromosomy

    def ocen(self):
        suma_A = self.chromosomy[0].sprawdz_atrakcyjnosc()
        suma_B = self.chromosomy[1].sprawdz_odpornosc()
        return A*suma_A, B*suma_B


def funkcja_oceny(populacja):
    sortowana_populacja = []
    for osoba in populacja:
        sortowana_populacja.append((osoba, osoba.ocen()))
    sortowana_populacja.sort(key=lambda x: (x[1][0], x[1][1]))
    oceniona_populacja = []
    suma_wsp = (len(populacja) + 1) / 2 * len(populacja)
    waga = suma_wsp/len(populacja)
    wagi = [i*waga for i in range(1, len(populacja)+1)]
    suma_wag = sum(wagi)
    for i in range(len(populacja)):
        oceniona_populacja.append((osoba, 100*wagi[i]/suma_wag))
    oceniona_populacja.sort(key=lambda x: x[1], reverse=True)
    return oceniona_populacja


def metoda_ruletki(oceniona_populacja, ile_wylosowanych):
    m = 0
    n = 0
    kolo = []
    for osoba, procent in oceniona_populacja:
        n += round(procent, 4)
        if n > 100:
            n = 100
        kolo.append((osoba, m, n))
        m = n+0.0001
    wylosowane_osoby = []
    wylosowane_liczby = random.sample([i/10000 for i in range(1000000)], ile_wylosowanych)
    for i in range(ile_wylosowanych):
        for k in kolo:
            if k[1] <= wylosowane_liczby[i] <= k[2]:
                wylosowane_osoby.append(k[0])
                break
    return wylosowane_osoby


def metoda_turnieju(populacja, wielkosc_turnieju):
    turniej1 = []
    for i in range(wielkosc_turnieju):
        turniej1.append(random.sample(populacja, wielkosc_turnieju))
    turniej2 = []
    for turniej in turniej1:
        turniej2.append(funkcja_oceny(turniej).pop()[0])
    return funkcja_oceny(turniej2).pop()[0]


def metoda_rankingowa(populacja, ile_osobnikow):
    if ile_osobnikow > len(populacja):
        raise ValueError("Przekroczono możliwą liczbę uczestników!")
    populacja_wagowa = funkcja_oceny(populacja)[:ile_osobnikow]
    top = []
    for osoba, waga in populacja_wagowa:
        top.append(osoba)
    return top


def krzyzowanie_jednopunktowe(X, Y):
    punkt_przeciecia = random.randint(0, 50)
    geny_x = X.chromosomy[0].geny
    geny_y = Y.chromosomy[0].geny
    geny_dziecka = geny_x[:punkt_przeciecia] + geny_y[punkt_przeciecia:]
    dziecko = OsobaA()
    dziecko.chromosomy[0].geny = geny_dziecka
    return dziecko


def krzyzowanie_dwupunktowe(X, Y):
    geny_x = X.chromosomy[0].geny
    geny_y = Y.chromosomy[0].geny
    punkt_przeciecia1 = random.randint(0, int(len(geny_x)/2))
    ogranicznik = int(input(f'Wprowadź ograniczenie drugiego podziału [{punkt_przeciecia1}-50]: \n'))
    punkt_przeciecia2 = random.randint(punkt_przeciecia1, ogranicznik)
    geny_dziecka = geny_x[:punkt_przeciecia1] + geny_y[punkt_przeciecia1:punkt_przeciecia2] + geny_x[punkt_przeciecia2:]
    dziecko = OsobaA()
    dziecko.chromosomy[0].geny = geny_dziecka
    return dziecko


def krzyzowanie_jednopunktoweB(X, Y):
    punkt_przeciecia0 = random.randint(0, 148)
    punkt_przeciecia1 = random.randint(0, 148)
    geny_x0 = X.chromosomy[0].geny
    geny_y0 = Y.chromosomy[0].geny
    geny_x1 = X.chromosomy[1].geny
    geny_y1 = Y.chromosomy[1].geny
    geny_dziecka0 = geny_x0[:punkt_przeciecia0] + geny_y0[punkt_przeciecia0:]
    geny_dziecka1 = geny_x1[:punkt_przeciecia1] + geny_y1[punkt_przeciecia1:]
    dziecko = OsobaB()
    dziecko.chromosomy[0].geny = geny_dziecka0
    dziecko.chromosomy[1].geny = geny_dziecka1
    return dziecko


def krzyzowanie_dwupunktoweB(X, Y):
    geny_x0 = X.chromosomy[0].geny
    geny_y0 = Y.chromosomy[0].geny
    geny_x1 = X.chromosomy[1].geny
    geny_y1 = Y.chromosomy[1].geny
    punkt_przeciecia1 = random.randint(0, int(len(geny_x0)/2))
    ogranicznik = int(input(f'Wprowadź ograniczenie drugiego podziału [{punkt_przeciecia1}-148]: \n'))
    punkt_przeciecia2 = random.randint(punkt_przeciecia1, ogranicznik)
    geny_dziecka0 = geny_x0[:punkt_przeciecia1] + geny_y0[punkt_przeciecia1:punkt_przeciecia2] + geny_x0[punkt_przeciecia2:]
    geny_dziecka1 = geny_x1[:punkt_przeciecia1] + geny_y1[punkt_przeciecia1:punkt_przeciecia2] + geny_x1[punkt_przeciecia2:]
    dziecko = OsobaB()
    dziecko.chromosomy[0].geny = geny_dziecka0
    dziecko.chromosomy[1].geny = geny_dziecka1
    return dziecko


def wybierz_selekcje():
    rodzice = []
    print("Wybierz metodę selekcji:")
    wybor = int(input("""1 - Koło ruletki
2 - Metoda rankingowa
3 - Metoda turniejowa\n"""))
    if wybor == 1:
        rodzice = metoda_ruletki(funkcja_oceny(POPULACJA), 2)
        dziecko = wybierz_krzyzowanie(rodzice)
    elif wybor == 2:
        rodzice = metoda_rankingowa(POPULACJA, 2)
        dziecko = wybierz_krzyzowanie(rodzice)
    elif wybor == 3:
        n = int(input("Wprowadż wielkość turnieju:\n"))
        rodzice = [metoda_turnieju(POPULACJA, n)]
        rodzice.append(metoda_turnieju(POPULACJA, n))
        dziecko = wybierz_krzyzowanie(rodzice)
    return rodzice[0]


def wybierz_krzyzowanie(rodzice):
    print("Wybierz metodę krzyżowania:")
    wybor = int(input("""1 - jednopunktowe
2 - dwupunktowe\n"""))
    if wybor == 1:
        krzyzowanie_jednopunktowe(rodzice[0], rodzice[1])
    elif wybor == 2:
        krzyzowanie_dwupunktowe(rodzice[0], rodzice[1])


def funkcja_eliminacji(populacja):
    nowa_generacja = []
    for osobnik in populacja:
        odpornosc = osobnik.ocen()[1]
        if 0.5 < odpornosc <= 0.6:
            if random.choices([0, 1], [0.05, 0.95])[0] == 1:
                nowa_generacja.append(osobnik)
        elif 0.4 < odpornosc <= 0.5:
            if random.choices([0, 1], [0.1, 0.9])[0] == 1:
                nowa_generacja.append(osobnik)
        elif odpornosc <= 0.4:
            if random.choices([0, 1], [0.15, 0.85])[0] == 1:
                nowa_generacja.append(osobnik)
        else:
            nowa_generacja.append(osobnik)
    return nowa_generacja


def oblicz_wspolczynniki(populacja):
    srednia_atrakcyjnosc = 0
    srednia_odpornosc = 0
    for osobnik in populacja:
        atrakcyjnosc, odpornosc = osobnik.ocen()
        srednia_atrakcyjnosc += atrakcyjnosc
        srednia_odpornosc += odpornosc
    srednia_atrakcyjnosc = srednia_atrakcyjnosc/len(populacja)
    srednia_odpornosc = srednia_odpornosc/len(populacja)
    return srednia_atrakcyjnosc, srednia_odpornosc


A = 1
B = 1


def trybA():
    global POPULACJA
    POPULACJA = []
    n = int(input("Wprowadź liczebność populacji:\n"))
    for i in range(n):
        POPULACJA.append(OsobaA())
    print(wybierz_selekcje())


def trybB():
    global POPULACJA
    POPULACJA = []
    n = int(input("Wprowadź liczebność populacji:\n"))
    for i in range(n):
        POPULACJA.append(OsobaB())
    WSPOLCZYNNIK_URODZEN = int(0.5 * len(POPULACJA))

    liczebnosc_populacji = []
    wspolczynniki_populacji = []
    for i in range(500):
        dzieci = []
        rodzice = metoda_ruletki(funkcja_oceny(POPULACJA), WSPOLCZYNNIK_URODZEN)
        rodzice = numpy.random.choice(rodzice, size=(int(len(rodzice)/2), 2), replace=False)
        for X, Y in rodzice:
            dziecko = krzyzowanie_jednopunktoweB(X, Y)
            dzieci.append(dziecko)
        POPULACJA.extend(dzieci)
        POPULACJA = funkcja_eliminacji(POPULACJA)
        liczebnosc_populacji.append(len(POPULACJA))
        wspolczynniki_populacji.append(oblicz_wspolczynniki(POPULACJA))
    plt.figure(0)
    plt.plot(liczebnosc_populacji)
    plt.title(f'Liczebnosc {A}, {B}')
    plt.figure(1)
    plt.title(f'Wsp populacji {A}, {B}')
    plt.plot(wspolczynniki_populacji)
    plt.show()


def wybierz_tryb():
    i = int(input("""Wybierz tryb działania programu: 
1 - tryb A
2 - tryb B\n"""))
    if i == 1:
        trybA()
    elif i == 2:
        trybB()


if __name__ == "__main__":
    wybierz_tryb()
