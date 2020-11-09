import base64

class Builder:
    def __init__(self, tablica):
        self.tablica = tablica

    def budujNaglowek(self):
        pass
    def budujTagi(self):
        pass
    def budujBody(self):
        pass

class wavBuilder(Builder):

    def budujNaglowek(self):
        return "WavHeader"

    def budujTagi(self):
        return ""

    def budujBody(self):
        return ", ".join(map(str, self.tablica))

class mp3Builder(Builder):

    def budujNaglowek(self):
        return "Mp3Header"

    def budujTagi(self):
        return "Mp3Tags"

    def budujBody(self):
        return base64.b64encode(b'zip(self.tablica)')

class OggBuilder(Builder):

    def budujNaglowek(self):
        return "OggHeader"

    def budujTagi(self):
        return "OggTags"

    def budujBody(self):
        for i in range(len(self.tablica)):
            if self.tablica[i] > 100:
                self.tablica[i] = 100
            if self.tablica[i] < -100:
                self.tablica[i] = -100
        return base64.b64encode(b'zip(self.tablica)')
class Kierownik:
    def __init__(self, budowniczy, tablica):
        self.budowniczy = budowniczy(tablica)

    def generujNapis(self):
        print(f'{self.budowniczy.budujNaglowek()} {self.budowniczy.budujTagi()} {self.budowniczy.budujBody()}')



if __name__ == "__main__":
    Kierownik(wavBuilder, [1,2]).generujNapis()
    Kierownik(mp3Builder, [5, 10]).generujNapis()
    Kierownik(OggBuilder, [6, 9]).generujNapis()