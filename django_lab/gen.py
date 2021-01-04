import random


class Chromosom:
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


class Osoba:
    def __init__(self, n):
        self.chromosomy = self.stworz_chromosomy(1)
        self.n = n

    def __repr__(self):
        return self.n

    def stworz_chromosomy(self, liczba_chromosomow):
        chromosomy = []
        for i in range(liczba_chromosomow):
            chr = Chromosom()
            for i in range(50):
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


def funkcja_oceny(populacja):
    sortowana_populacja = []
    for osoba in populacja:
        sortowana_populacja.append((osoba, osoba.ocen()))
    sortowana_populacja.sort(key=lambda x: (x[1][0], x[1][1]))
    suma_wag = (len(populacja)+1)/2*len(populacja)
    oceniona_populacja = []
    for id, (osoba, _) in enumerate(sortowana_populacja):
        oceniona_populacja.append((osoba, 100*(id+1)/suma_wag))
    oceniona_populacja.sort(key=lambda x: x[1], reverse=True)
    return oceniona_populacja

def metoda_ruletki(oceniona_populacja, ile_wylosowanych):
    m = 0
    n = 0
    kolo = []
    for osoba, procent in oceniona_populacja:
        n += round(procent)
        if n > 100:
            n = 100
        kolo.append((osoba, m, n))
        m = n+1
    print(kolo)
    dodatkowe_losowanie = 0
    wylosowane_osoby = []
    wylosowane_liczby = random.sample(range(100), ile_wylosowanych)
    for i in range(ile_wylosowanych):
        for k in kolo:
            if k[1] <= wylosowane_liczby[i] <= k[2]:
                if k[0] in wylosowane_osoby:
                    dodatkowe_losowanie += 1
                else:
                    wylosowane_osoby.append(k[0])
    while dodatkowe_losowanie > 0:
        x = random.randint(0, 100)
        for k in kolo:
            if k[1] <= x <= k[2]:
                if k[0] not in wylosowane_osoby:
                    wylosowane_osoby.append(k[0])
                    dodatkowe_losowanie -= 1
    return wylosowane_osoby

def metoda_turnieju(populacja, wielkosc_turnieju):
    print('turniuej', populacja)
    turniej1 = []
    for i in range(wielkosc_turnieju):
        turniej1.append(random.sample(populacja, wielkosc_turnieju))
    print(turniej1)
    turniej2 = []
    for turniej in turniej1:
        turniej2.append(funkcja_oceny(turniej).pop()[0])
    print(turniej2)
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
    dziecko = Osoba("dziecko")
    dziecko.chromosomy[0].geny = geny_dziecka
    return dziecko

def krzyzowanie_dwupunktowe(X, Y):
    geny_x = X.chromosomy[0].geny
    geny_y = Y.chromosomy[0].geny
    punkt_przeciecia1 = random.randint(0, int(len(geny_x)/2))
    punkt_przeciecia2 = random.randint(punkt_przeciecia1, 50)
    geny_dziecka = geny_x[:punkt_przeciecia1] + geny_y[punkt_przeciecia1:punkt_przeciecia2] + geny_x[punkt_przeciecia2:]
    dziecko = Osoba("dziecko")
    dziecko.chromosomy[0].geny = geny_dziecka
    return dziecko

# print(funkcja_oceny(P))
# print(metoda_ruletki(funkcja_oceny(P), 6))
# print(metoda_turnieju(P, 2))
# print(metoda_rankingowa(P, 2))
# print(krzyzowanie_jednopunktowe(d, b))
#krzyzowanie_dwupunktowe(a, ab)
POPULACJA = []
# n = int(input("Wprowadź liczebność populacji:\n"))
# for i in range(n):
#     POPULACJA.append(Osoba())
a = Osoba("A")
ab = Osoba("Ab")
b = Osoba("B")
c = Osoba("C")
d = Osoba("D")
e = Osoba("E")
a.chromosomy[0].geny = [9, 0, 9, 0, 1, 1, 2]
ab.chromosomy[0].geny = [9, 1, 9, 3, 6, 6, 4]
b.chromosomy[0].geny = [0, 9, 0, 9]
c.chromosomy[0].geny = [1, 9, 1, 9]
d.chromosomy[0].geny = [1, 1, 1, 1]
e.chromosomy[0].geny = [1, 1, 1, 2]
P = [a, b, c, d, e, ab]
