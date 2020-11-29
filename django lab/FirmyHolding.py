import json
from dict2xml import dict2xml


class Firma:

    def __init__(self, nazwa, adres, NIP, przychody, dochody, kontrahenci):
        self.nazwa = nazwa
        self.adres = adres
        self.NIP = NIP
        self.przychody = przychody
        self.dochody = dochody
        self.kontrahenci = kontrahenci
        self.nagroda = 0

    def dodaj(self, firma):
        self.kontrahenci.append(firma)

    def zwroc_nazwe(self):
        return self.nazwa

    def zwroc_NIP(self):
        return [self.NIP]

    def zwroc_nagrode(self):
        return self.nagroda

    def czy_zlota(self):
        if self.przychody > 100000:
            return 1
        else:
            return 0
    def akceptuj_wizytatora(self, wizytator):
        wizytator.pobierz_firme(self)

    def zwroc_slownik(self):
        slownik = {"Nazwa":self.nazwa, "Adres":self.adres, "NIP":self.NIP, "Przychody":self.przychody, "Dochody":self.dochody}
        slownik["Kontrahenci"] = []
        if len(self.kontrahenci) > 0:
            for firma in self.kontrahenci:
                slownik["Kontrahenci"].append(firma.zwroc_slownik())
        return slownik



class GrupaFirm(Firma):

    def __init__(self):
        self._firmy = []

    def dodaj(self, firma):
        self._firmy.append(firma)

    def zwroc_nazwe(self):
        nazwy = []
        for i in self._firmy:
            nazwy.append(i.zwroc_nazwe())
        return f"Firmy({'+'.join(nazwy)})"

    def zwroc_NIP(self):
        NIPy = []
        for i in self._firmy:
            NIPy.extend(i.zwroc_NIP())
        return NIPy

    def zwroc_nagrode(self):
        nagrody = 0
        for firma in self._firmy:
            nagrody += firma.zwroc_nagrode()
        return nagrody

    def czy_zlota(self):
        liczba_zlotych = 0
        for firma in self._firmy:
            liczba_zlotych += firma.czy_zlota()
        return liczba_zlotych

    def akceptuj_wizytatora(self, wizytator):
        wizytator.pobierz_wiele_firm(self)

    def zwroc_slownik(self):
        slownik = {}
        for firma in self._firmy:
            slownik[firma.zwroc_nazwe()] = firma.zwroc_slownik()
        return slownik



class Bonifikata(Firma):

    def __init__(self, firma):
        self._firma = firma

    @property
    def firma(self):
        return self._firma

    def zwroc_NIP(self):
        return self._firma.zwroc_NIP()

    def zwroc_nagrode(self):
        return self._firma.zwroc_nagrode()

    def czy_zlota(self):
        return self._firma.czy_zlota()



class Nieparzyste(Bonifikata):

    def zwroc_nagrode(self):
        suma_nagrod = 0
        for NIP in self.zwroc_NIP():
            if [True for char in NIP if int(char) % 2 == 1].count(True)==10:
                suma_nagrod += 50
        return super().zwroc_nagrode() + suma_nagrod

class Podzielneprzez3(Bonifikata):

    def zwroc_nagrode(self):
        suma_nagrod = 0
        for NIP in self.zwroc_NIP():
            if [True for char in NIP if int(char) % 3 == 0].count(True)>=5:
                suma_nagrod += 100
        return super().zwroc_nagrode() + suma_nagrod

class CyfryDniaMMDD(Bonifikata):

    def zwroc_nagrode(self):
        suma_nagrod = 0
        for NIP in self.zwroc_NIP():
            if MMDD in NIP:
                suma_nagrod += 15
        return super().zwroc_nagrode() + suma_nagrod

class CyfryDniaMMDDx3(Bonifikata):

    def zwroc_nagrode(self):
        suma_nagrod = 0
        suma_dni_i_miesiecy = 0
        for i in MMDD:
            suma_dni_i_miesiecy += int(i)
        for NIP in self.zwroc_NIP():
            if sum([int(char) for char in NIP]) == suma_dni_i_miesiecy*3:
                suma_nagrod += 550
        return super().zwroc_nagrode() + suma_nagrod


class SumaWartosciBezwzglednych(Bonifikata):

    def zwroc_nagrode(self):
        suma_nagrod = 0
        for NIP in self.zwroc_NIP():
            if sum([abs(int(NIP[i+1])-int(NIP[i])) for i in range(len(NIP)-1)]) > 50:
                suma_nagrod += 200
        return super().zwroc_nagrode() + suma_nagrod

class ZlotyLaur(Bonifikata):

    def zwroc_nagrode(self):
        suma_nagrod = super().czy_zlota() * 30
        return super().zwroc_nagrode() + suma_nagrod


class WizytatorJSON:
    def pobierz_firme(self, firma):
        data = firma.zwroc_slownik()
        return json.dumps(data)
    def pobierz_wiele_firm(self, firmy):
        data = firmy.zwroc_slownik()
        return json.dumps(data)
class WizytatorXML:
    def pobierz_firme(self, firma):
        data = firma.zwroc_slownik()
        return dict2xml(data)
    def pobierz_wiele_firm(self, firmy):
        data = firmy.zwroc_slownik()
        return dict2xml(data)

MMDD = "1611"

nieparzysta = Firma("Firma1", "X", "1133557799", 5000, 4000, [])
podzielna3 = Firma("Firma2", "X", "9996612121", 5000, 4000, [nieparzysta])
mmdd = Firma("Firma3", "X", "1611000000", 5000, 4000, [nieparzysta, podzielna3])
mmdd3 = Firma("Firma4", "X", "1611161118", 5000, 4000, [nieparzysta, podzielna3, mmdd])
bezwzgledne = Firma("Firma5", "X", "0909090500", 5000, 4000, [])
zlota = Firma("Firma6", "X", "0909090500", 105000, 4000, [])
zwykla = Firma("Firma7", "X", "0909090500", 5000, 4000, [])

spolka1 = GrupaFirm()
spolka1.dodaj(nieparzysta)
spolka1.dodaj(podzielna3)
spolka1.dodaj(mmdd)
spolka1.dodaj(mmdd3)
spolka1.dodaj(bezwzgledne)
spolka1.dodaj(zlota)

spolka2 = GrupaFirm()
spolka2.dodaj(spolka1)
spolka2.dodaj(zwykla)

spolka3 = GrupaFirm()
spolka3.dodaj(spolka2)
spolka3.dodaj(zwykla)



print("Nazwa pojedynczej klasy\t", nieparzysta.zwroc_nazwe())
print("Numer NIP pojedynczej klasy\t",nieparzysta.zwroc_NIP())

print("Kontrahenci Spółki3\t",spolka3.zwroc_nazwe())
print("Numery NIP Spółki3\t", spolka3.zwroc_NIP())
print("Wartość bonifikaty dla Spółki3\t", Nieparzyste(Podzielneprzez3(CyfryDniaMMDD(CyfryDniaMMDDx3(SumaWartosciBezwzglednych(ZlotyLaur(spolka3)))))).zwroc_nagrode())

wizytatorXML = WizytatorXML()
print(wizytatorXML.pobierz_firme(nieparzysta))
print(wizytatorXML.pobierz_wiele_firm(spolka1))

wizytatorJSON = WizytatorJSON()
print(wizytatorJSON.pobierz_firme(nieparzysta))
print(wizytatorJSON.pobierz_wiele_firm(spolka1))
