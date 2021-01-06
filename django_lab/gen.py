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
    def __init__(self):
        self.chromosomy = self.stworz_chromosomy(1)

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
    dziecko = Osoba()
    dziecko.chromosomy[0].geny = geny_dziecka
    return dziecko

def krzyzowanie_dwupunktowe(X, Y):
    geny_x = X.chromosomy[0].geny
    geny_y = Y.chromosomy[0].geny
    punkt_przeciecia1 = random.randint(0, int(len(geny_x)/2))
    ogranicznik = int(input(f'Wprowadź ograniczenie drugiego podziału [{punkt_przeciecia1}-50]: \n'))
    punkt_przeciecia2 = random.randint(punkt_przeciecia1, ogranicznik)
    geny_dziecka = geny_x[:punkt_przeciecia1] + geny_y[punkt_przeciecia1:punkt_przeciecia2] + geny_x[punkt_przeciecia2:]
    dziecko = Osoba()
    dziecko.chromosomy[0].geny = geny_dziecka
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

POPULACJA = []
n = int(input("Wprowadź liczebność populacji:\n"))
for i in range(n):
    POPULACJA.append(Osoba())
print(wybierz_selekcje())