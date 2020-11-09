napis = """k1: w2
k2: w2
k3: w3"""
def zrobslownik(napis):
    slownik = dict()
    for i in napis.split("\n"):
        key, value = i.split(":")
        slownik[key] = value.strip()
    return slownik

def zrobslownikzpliku(plik):
    slownik = dict()
    with open(plik, "r") as f:
        for i in f.readlines():
            key, value = i.split(":")
            slownik[key] = value.strip()
    return slownik
def zliczslowa(plik):
    with open(plik, "r") as f:
        text = f.read()
    for char in '-.,\n':
        text = text.replace(char, ' ')
    word_list = text.split()
    d = {}
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    return d
def cezar(plik1, plik2):
    with open(plik1, "r") as f:
        file = f.read()
    KLUCZ = 3
    zaszyfrowny = ""
    for i in range(len(file)):
        if ord(file[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(file[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(file[i]) + KLUCZ)
    with open(plik2, "w") as f:
        f.write(zaszyfrowny)

def porownajpliki(plik1, plik2, plik3):
    plik = []
    plikB = []
    with open(plik1, "r") as f:
        for line in f.readlines():
            plik.append(line)
    with open(plik2, "r") as f:
        for line in f.readlines():
            if line in plik:
                plik.remove(line)
            else:
                plikB.append(line)
    with open(plik3, "w") as f:
        for i in plik:
            f.write(i)
        for i in plikB:
            f.write(i)
#zrobslownik(napis)
#zrobslownikzpliku("plik.txt")
#zliczslowa("plik.txt")
#cezar("plik1", "plik2")
#porownajpliki("plik1", "plik2", "plik3")
import os

def pierwsze(napis):
    return [(x, len(x)) for x in napis.split(" ")]

def fibo():
    n = int(input("Wprowadz liczbe: "))
    numbers = [0, 1]
    [numbers.append(numbers[k-1]+numbers[k-2]) for k in range(2,n)]
    return numbers

def f1(func, list):
    return func(list)
def wiekszeod10(list):
    return [x for x in list if x > 10]

def odleglosc_punktow(punkty, docelowy):
    odl = []
    for i in punkty:
        l = ((docelowy[0] - i[0])**2+(docelowy[1] - i[1])**2)**0.5
        odl.append((l, i))
    return sorted(odl)

def generator():
    rozszerzenie = input("Rozszerzenie")
    sciezka = input("Ścieżka")
    for file in os.listdir(sciezka):
        print("a", file)
        if file.endswith(rozszerzenie):
            yield file

#print(pierwsze("To jest tekst przykładowy."))
#print(fibo())
#print(f1(wiekszeod10, [1,2,30,50]))
#print(odleglosc_punktow([(0,0), (1,1), (2,2), (3,3), (-1, 0)], (-3, -8)))
#print(next(generator(".sh", ".")))
class liczbaZespolona:
    def __init(self, re, im):
        self.re = re
        self.im = im
    def __add__(self, other):
        self.re += other.re
        self.im += other.im
    def __sub__(self, other):
        self.re -= other.re
        self.im -= other.im
    def __mul__(self, other):
        self.re *= other.re
        self.im *= other.im
    def __truediv__(self, other):
        self.re /= other.re
        self.re /= other.im
    def modul(self):
        return (self.re**2+self.im**2)**0.5
    def __lt__(self, other):
        if self.modul() < other.modul():
            return True
        else:
            return False
    def __gt__(self, other):
        if self.modul() > other.modul():
            return True
        else:
            return False
    def __repr__(self):
        return f'{self.re} + {self.im}i'

class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def odleglosc(self, a, b):
        return ((a-self.x)**2+(b-self.y)**2)**0.5

class Punkt3D(Punkt2D):
    def __init__(self, x, y, z):
        super(Punkt3D, self).__init__(x,y)
        self.z = z
    def odleglosc(self, a, b, c):
        return ((a-self.x)**2+(b-self.y)**2+(c-self.z)**2)**0.5

class Liczba:
    def __init__(self, x):
        self.cyfry = str(x).split()
        self.waga = int(x)
    def __mul__(self, other):
        self.waga *= other
    def silnia(self, n):
        f = lambda x: x * f(x-1) if x != 0 else 1
        return f(n)
import string
#for a, b in zip(string.ascii_lowercase, string.ascii_uppercase):
#    print(f'{a} {b} ', end="")
#text = input("Tekst do zaszyfrowania:\n")
#for i in text:
#    print(chr(ord(i)%57+58), end="")
