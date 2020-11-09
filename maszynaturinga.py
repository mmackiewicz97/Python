import collections
import sys


class Tasma:
    def __init__(self, slowo):
        self.tasma = collections.OrderedDict(enumerate(slowo))

    def __str__(self):
        return "___"+"".join(self.tasma.values())+"___"

    def __getitem__(self, index):
        return self.tasma[index]

    def __setitem__(self, index, znak):
        self.tasma[index] = znak

    def zwroc_slowo(self):
        s = "".join(self.tasma.values())
        return s[:-1]


class MaszynaTuringa:
    def __init__(self, plik, opis, stany, alfabet, slowo, stan_kon, instrukcja):
        try:
            for i in slowo:
                if i not in alfabet:
                    raise ValueError(f'Napotkano błąd! Znak "{i}" nie występuje w alfabecie: {alfabet}.')
        except ValueError as e:
            print(e)
            sys.exit(1)
        self.plik = plik
        self.opis = opis
        self.stany = stany
        self.alfabet = alfabet
        self.slowo = slowo

        self.stan_akt = stany[0]
        self.stan_kon = stan_kon
        self.instrukcja = instrukcja
        self.tasma = Tasma(self.slowo+"_")
        self.poz = 0
        self.zakoncz = False
        print(f'Program: {opis}')

    def pokaz(self):
        print(self.tasma)
        print(" "*(2+self.poz), "|")
        print(f'Aktualny stan: {self.stan_akt}')
        print("")

    def krok(self):
        self.pokaz()
        znak_akt = self.tasma[self.poz]
        stan, znak, ruch = self.instrukcja[self.stan_akt][znak_akt]
        if stan in self.instrukcja.keys() or stan in self.stan_kon:
            self.stan_akt = stan
        else:
            raise ValueError(f'Napotkano błąd! Stan: "{stan}" spoza zakresu: {self.stany}')
        if znak in self.alfabet:
            self.tasma[self.poz] = znak
        else:
            raise ValueError(f'Napotkano błąd! Znak: "{znak}" nie występuje w alfabecie. Poprawny znaki to: {self.alfabet}')
        if ruch == "r":
            self.poz += 1
        elif ruch == "l":
            self.poz -= 1
        elif ruch == "s":
            self.zakoncz = True
        else:
            raise ValueError(f'Napotkano błąd! Ruch: "{ruch}" niezdefiniowany. Możliwe ruchy to "l" lub "r".')

    def koniec(self):
        if self.stan_akt in self.stan_kon or  self.zakoncz is True:
            return True
        else:
            return False

    def dzialanie(self, max_iteracja=999):
        iteracja = 0
        try:
            while not self.koniec():
                self.krok()
                if iteracja > max_iteracja:
                    raise BufferError(f'Napotkano błąd! Przekroczono maksymalną liczbę iteracji - {max_iteracja}.')
                iteracja += 1
            print(f'Program zakończył w stanie: {self.stan_akt}')
        except (ValueError, BufferError) as e:
            print(e)
            sys.exit(1)
        with open(f'{self.plik}_wynik.txt', "w") as f:
            f.write("Początkowe słowo: "+self.slowo+"\n")
            f.write("Opis: "+self.opis+"\n")
            f.write("Wynik programu: "+self.tasma.zwroc_slowo()+"\n")
            f.write(f'Program zakończył w stanie: {self.stan_akt}')


def wczytaj(plik):
    with open(plik, "r") as f:
        dane_wej = []
        for linia in f.readlines():
            dane_wej.append(linia.rstrip())
        opis = dane_wej.pop(0)
        stany = dane_wej.pop(0).split(",")
        alfabet = dane_wej.pop(0).split(",")
        slowo = dane_wej.pop(0)
        stan_kon = dane_wej.pop(0).split(",")
        instrukcja = {}
        for i in range(len(stany)):
            akt_stan = stany[i]
            if akt_stan != "k":
                nowy_stan = stany[i+1]
                if nowy_stan != "k":
                    lista = dane_wej[1:dane_wej.index(nowy_stan+":")]
                    rozkazy = {}
                    for x in lista:
                        rozkazy[x[0]] = x[2:].replace(";", "").split(",")
                    instrukcja[akt_stan] = rozkazy
                else:
                    lista = dane_wej[dane_wej.index(akt_stan+":")+1:]
                    rozkazy = {}
                    for x in lista:
                        rozkazy[x[0]] = x[2:].replace(";", "").split(",")
                    instrukcja[akt_stan] = rozkazy
        return plik, opis, stany, alfabet, slowo, stan_kon, instrukcja


maszyna1 = MaszynaTuringa(*wczytaj("7"))
maszyna1.dzialanie()
maszyna2 = MaszynaTuringa(*wczytaj("8"))
maszyna2.dzialanie()
maszyna3 = MaszynaTuringa(*wczytaj("9"))
maszyna3.dzialanie()
