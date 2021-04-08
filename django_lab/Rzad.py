Ustawa_tarcza_kryzysowa = {
    "1":
        {
            "1": "Treść paragrafu 1",
            "2": "Treść paragrafu 2",
            "3": "Treść paragrafu 3",
        },
    "2":
        {
            "1": "Treść paragrafu 1",
            "2": "Treść paragrafu 2",
            "3": "Treść paragrafu 3",
        },
}
Ustawa_COVID = {
    "1":
        {
            "1": "Treść paragrafu 1",
            "2": "Treść paragrafu 2",
            "3": "Treść paragrafu 3",
        },
    "2":
        {
            "1": "Treść paragrafu 1",
            "2": "Treść paragrafu 2",
            "3": "Treść paragrafu 3",
        },
}
class Zmiana:

    def wykonaj(self):
        pass


class ZmianaParagrafuTarczy(Zmiana):

    def __init__(self, wykonawca, paragraf, nowa_tresc):
        self.wykonawca = wykonawca
        self.paragraf = paragraf
        self.nowa_tresc = nowa_tresc

    def wykonaj(self):
        self.wykonawca.zmien_ustawe_tarcze(self.wykonawca, self.paragraf, self.nowa_tresc)


class ZmianaParagrafuCOVID(Zmiana):

    def __init__(self, wykonawca, paragraf, nowa_tresc):
        self.wykonawca = wykonawca
        self.paragraf = paragraf
        self.nowa_tresc = nowa_tresc

    def wykonaj(self):
        self.wykonawca.zmien_ustawe_COVID(self.wykonawca, self.paragraf, self.nowa_tresc)

class Wykonawca:

    def zmien_ustawe_tarcze(self, paragraf, tresc):
        pass

    def zmien_ustawe_COVID(self, paragraf, tresc):
        pass

class PodWykonawca(Wykonawca):

    def zmien_ustawe_tarcze(self, paragraf, tresc):
        global Ustawa_tarcza_kryzysowa
        Ustawa_tarcza_kryzysowa[paragraf] = tresc
        return Ustawa_tarcza_kryzysowa

    def zmien_ustawe_COVID(self, paragraf, tresc):
        global Ustawa_COVID
        Ustawa_COVID[paragraf] = tresc
        return Ustawa_COVID

class Rzad:
    def zaktualizuj_ustawe(self, ustawa, paragraf, tresc):
        if ustawa == "COVID":
            ZmianaParagrafuCOVID(PodWykonawca, paragraf, tresc).wykonaj()
        else:
            ZmianaParagrafuTarczy(PodWykonawca, paragraf, tresc).wykonaj()
rzad = Rzad()
print(Ustawa_tarcza_kryzysowa)
rzad.zaktualizuj_ustawe("Tarcza", "1", {"1":"1500 plus dla bezrobotnych"})
rzad.zaktualizuj_ustawe("Tarcza", "2", {"2":"500 plus dla przedsiebiorcow"})
print(Ustawa_tarcza_kryzysowa)
print(Ustawa_COVID)
rzad.zaktualizuj_ustawe("COVID", "1", {"1":"Zmiana 1"})
rzad.zaktualizuj_ustawe("COVID", "2", {"2":"Zmiana 2"})
print(Ustawa_COVID)

