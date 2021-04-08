NAUCZYCIELSKIE_STOPNIE_AWANSU = ["Nauczyciel stażysta", "Nauczyciel kontraktowy", "Nauczyciel mianowany", "Nauczyciel Dyplomowany"]

class Pracownik:
    def __init__(self, imie, nazwisko, stopien_awansu, pensja, stanowisko_kierownicze=None, dodatek_stanowiskowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stopien_awansu = stopien_awansu
        self.pensja = pensja
        self.stanowisko_kierownicze = stanowisko_kierownicze
        self.dodatek_stanowiskowy = dodatek_stanowiskowy
    def zwykly_awans(self):
        pass
    def kierowniczy_awans(self):
        pass
    def degradacja_zwykla(self):
        pass
    def degradacja_kierownicza(self):
        pass