import pygame
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN
from pygame.locals import KEYDOWN, K_RETURN, K_SPACE


class Plansza:
    def __init__(self, szer, wys):
        self.powierzchnia = pygame.display.set_mode((szer, wys))
        pygame.display.set_caption("Automat komórkowy")

    def rysuj(self, komorki):
        tlo = (0, 0, 0)
        self.powierzchnia.fill(tlo)
        komorki.rysuj_zyjace(self.powierzchnia)
        pygame.display.update()


class Komorki:
    def __init__(self, szer, wys, S, B, rozmiar):
        self.S = S
        self.B = B
        self.rozmiar = rozmiar
        self.szer = szer
        self.wys = wys
        self.pokolenie = self.reset()
        self.dodaj_stale()
        self.dodaj_oscylatory()
        self.dodaj_niestale()
        self.dodaj_statki()

    def reset(self):
        return [[0 for y in range(self.wys)] for x in range(self.szer)]

    def narysuj_myszka(self):
        przyciski = pygame.mouse.get_pressed()
        if not any(przyciski):
            return
        if przyciski[0]:
            komorka = True
        else:
            komorka = False
        x, y = pygame.mouse.get_pos()
        x = int(x / self.rozmiar)
        y = int(y / self.rozmiar)
        self.pokolenie[x][y] = 1 if komorka else 0

    def rysuj_zyjace(self, powierzchnia):
        for x, y in self.zyjace_komorki():
            kwadrat = (self.rozmiar, self.rozmiar)
            pozycja = (x * self.rozmiar, y * self.rozmiar)
            pygame.draw.rect(powierzchnia, (255, 255, 255), pygame.locals.Rect(pozycja, kwadrat), 1)

    def dodaj_stale(self):
        # kwadrat
        self.pokolenie[2][1] = 1
        self.pokolenie[2][2] = 1
        self.pokolenie[3][1] = 1
        self.pokolenie[3][2] = 1
        # łódź
        self.pokolenie[1][6] = 1
        self.pokolenie[1][7] = 1
        self.pokolenie[2][6] = 1
        self.pokolenie[2][8] = 1
        self.pokolenie[3][7] = 1
        # kryształ
        self.pokolenie[1][15] = 1
        self.pokolenie[2][14] = 1
        self.pokolenie[2][16] = 1
        self.pokolenie[3][14] = 1
        self.pokolenie[3][16] = 1
        self.pokolenie[4][15] = 1

    def dodaj_oscylatory(self):
        # blinker
        self.pokolenie[12][2] = 1
        self.pokolenie[12][3] = 1
        self.pokolenie[12][4] = 1
        # żaba
        self.pokolenie[13][6] = 1
        self.pokolenie[12][7] = 1
        self.pokolenie[12][8] = 1
        self.pokolenie[14][9] = 1
        self.pokolenie[15][7] = 1
        self.pokolenie[15][8] = 1

    def dodaj_niestale(self):
        # die hard
        self.pokolenie[30][11] = 1
        self.pokolenie[31][11] = 1
        self.pokolenie[31][12] = 1
        self.pokolenie[35][12] = 1
        self.pokolenie[36][10] = 1
        self.pokolenie[36][12] = 1
        self.pokolenie[37][12] = 1

    def dodaj_statki(self):
        # glider
        self.pokolenie[1][21] = 1
        self.pokolenie[1][22] = 1
        self.pokolenie[2][20] = 1
        self.pokolenie[2][21] = 1
        self.pokolenie[0][20] = 1
        # dakota
        self.pokolenie[9][22] = 1
        self.pokolenie[9][24] = 1
        self.pokolenie[12][22] = 1
        self.pokolenie[13][23] = 1
        self.pokolenie[13][24] = 1
        self.pokolenie[13][25] = 1
        self.pokolenie[12][25] = 1
        self.pokolenie[11][25] = 1
        self.pokolenie[10][25] = 1

    def zyjace_komorki(self):
        for x in range(len(self.pokolenie)):
            kolumna = self.pokolenie[x]
            for y in range(len(kolumna)):
                if kolumna[y] == 1:
                    yield x, y

    def zwroc_sasiadow(self, x, y):
        # warunki brzegowe periodyczne
        # przenikające
        # sąsiedztwo Moora
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if nx == x and ny == y:
                    continue
                if nx >= self.szer:
                    nx = 0
                elif nx < 0:
                    nx = self.szer - 1
                if ny >= self.wys:
                    ny = 0
                elif ny < 0:
                    ny = self.wys - 1
                yield self.pokolenie[nx][ny]

    def stworz_nastepne_pokolenie(self):
        nastepni = self.reset()
        for x in range(len(self.pokolenie)):
            kolumna = self.pokolenie[x]
            for y in range(len(kolumna)):
                liczba_sasiadow = sum(self.zwroc_sasiadow(x, y))
                if liczba_sasiadow in self.B:
                    nastepni[x][y] = 1
                elif liczba_sasiadow in self.S:
                    nastepni[x][y] = kolumna[y]  # bez zmiany stanu
                else:
                    nastepni[x][y] = 0
        self.pokolenie = nastepni


class Automat:
    def __init__(self, szer, wys, S, B, rozmiar=20):
        pygame.init()
        self.plansza = Plansza(szer * rozmiar, wys * rozmiar)
        self.zegar = pygame.time.Clock()
        self.komorki = Komorki(szer, wys, S, B, rozmiar)
        self.start = None

    def dzialaj(self):
        while not self.zdarzenie():
            self.plansza.rysuj(self.komorki)
            if getattr(self, "start", None):
                self.komorki.stworz_nastepne_pokolenie()
            self.zegar.tick(5)

    def zdarzenie(self):
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            if zdarzenie.type == MOUSEMOTION or zdarzenie.type == MOUSEBUTTONDOWN:
                self.komorki.narysuj_myszka()
            if zdarzenie.type == KEYDOWN and zdarzenie.key == K_RETURN:
                if self.start is None:
                    self.start = True
                else:
                    self.start = None
            if zdarzenie.type == KEYDOWN and zdarzenie.key == K_SPACE:
                self.komorki.stworz_nastepne_pokolenie()


if __name__ == "__main__":
    S = [2, 3]  # przezywaja
    B = [3]  # tworza sie
    automat = Automat(50, 30, S, B)
    automat.dzialaj()
