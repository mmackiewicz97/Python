import random
import math
import networkx as nx
import matplotlib.pyplot as plt

KOLOR = ["czerwony", "niebieski"]

class Graf:
    def __init__(self, liczba_wierzcholkow, liczba_krawedzi):
        self.liczba_wierzcholkow = liczba_wierzcholkow
        self.liczba_krawedzi = liczba_krawedzi
        self.wierzcholki = []
        self.czy_dwudzielny = True
    def dodaj(self, v, w):
        for x in self.wierzcholki:
            if x.numer == v:
                x.sasiedzi.append(w)
                return
        x = Wierzcholek(v)
        x.sasiedzi.append(w)
        self.wierzcholki.append(x)
    def wyswietl_wierzcholki(self):
        for x in self.wierzcholki:
            print(x)
        print("")
    def wyswietl_kolor(self):
        for x in self.wierzcholki:
            print(x.zwroc_kolor())
    def zwroc_sasiadow(self, v, algorytm):
        for x in self.wierzcholki:
            if x.numer == v:
                if algorytm == "BFS":
                    return x.sasiedzi
                elif algorytm == "DFS":
                    return x.sasiedzi[::-1]
    def ustaw_kolor(self, v, kolor, printowanie):
        for x in self.wierzcholki:
            if x.numer == v:
                if x.kolor:
                    if x.kolor != kolor:
                        if printowanie is True:
                            print(f'Graf niedwudzielny!  Wierzchołek: {x.numer} ma ustawiony kolor {x.kolor}. Próbujesz zmienić na {kolor}.')
                        self.czy_dwudzielny = False
                        return 1
                else:
                    if printowanie is True:
                        print(f'Ustawiam kolor wierzcholka {x.numer} na kolor {kolor}')
                    x.kolor = kolor

class Wierzcholek:
    def __init__(self, numer):
        self.numer = numer
        self.sasiedzi = []
        self.kolor = None
    def __repr__(self):
        return f'Wierzchołek: {self.numer} - sąsiedzi: {"-".join(map(str,self.sasiedzi))}'
    def zwroc_kolor(self):
        return f'Wierzchołek: {self.numer} - kolor: {self.kolor}'

def algorytm_BFS(graf):
    print("/"*10+" ALGORYTM BFS "+"\\"*10)
    print("")
    graf.wyswietl_wierzcholki()
    odwiedzeni = []
    graf.ustaw_kolor(1, KOLOR[1], True)
    kolejka = [1]
    x = 1
    while kolejka:
        print(f'Krok: {x}')
        x += 1
        aktualny_wierzcholek = kolejka.pop(0)
        try:
            dodawani = graf.zwroc_sasiadow(aktualny_wierzcholek, "BFS")
            dodawani = [wierzcholek for wierzcholek in dodawani if wierzcholek not in odwiedzeni]
            nrkoloru = KOLOR.index(graf.wierzcholki[aktualny_wierzcholek-1].kolor)
            for wierzcholek in dodawani:
                graf.ustaw_kolor(wierzcholek, KOLOR[(nrkoloru+1)%2], True)
            dodawani = [wierzcholek for wierzcholek in dodawani if wierzcholek not in kolejka]
            kolejka.extend(dodawani)
        except:
            pass
        odwiedzeni.append(aktualny_wierzcholek)
        print(f'Odwiedzone: {"".join(map(str, odwiedzeni))}, na stosie: {"".join(map(str, kolejka))}')
    print("")
    print(f'Czy graf dwudzielny: {graf.czy_dwudzielny}')
    print("")
    graf.wyswietl_kolor()

def algorytm_DFS(graf):
    print("/"*10+" ALGORYTM DFS "+"\\"*10)
    print("")
    graf.wyswietl_wierzcholki()
    odwiedzeni = []
    graf.ustaw_kolor(1, KOLOR[1], True)
    kolejka = [1]
    x = 1
    while kolejka:
        print(f'Krok: {x}')
        x += 1
        aktualny_wierzcholek = kolejka.pop()
        try:
            dodawani = graf.zwroc_sasiadow(aktualny_wierzcholek, "DFS")
            dodawani = [wierzcholek for wierzcholek in dodawani if wierzcholek not in odwiedzeni]
            nrkoloru = KOLOR.index(graf.wierzcholki[aktualny_wierzcholek-1].kolor)
            for wierzcholek in dodawani:
                graf.ustaw_kolor(wierzcholek, KOLOR[(nrkoloru+1)%2], True)
            dodawani = [wierzcholek for wierzcholek in dodawani if wierzcholek not in kolejka]
            kolejka.extend(dodawani)
        except:
            pass
        odwiedzeni.append(aktualny_wierzcholek)
        print(f'Odwiedzone: {"".join(map(str, odwiedzeni))}, na stosie: {"".join(map(str, kolejka))}')
    print("")
    print(f'Czy graf dwudzielny: {graf.czy_dwudzielny}')
    print("")
    graf.wyswietl_kolor()

def algorytm_DFS_bez_print(graf):
    odwiedzeni = []
    graf.ustaw_kolor(1, KOLOR[1], False)
    kolejka = [1]
    while kolejka:
        aktualny_wierzcholek = kolejka.pop()
        try:
            dodawani = graf.zwroc_sasiadow(aktualny_wierzcholek, "DFS")
            dodawani = [wierzcholek for wierzcholek in dodawani if wierzcholek not in odwiedzeni]
            nrkoloru = KOLOR.index(graf.wierzcholki[aktualny_wierzcholek-1].kolor)
            for wierzcholek in dodawani:
                if graf.ustaw_kolor(wierzcholek, KOLOR[(nrkoloru+1)%2], False) == 1:
                    return False
            dodawani = [wierzcholek for wierzcholek in dodawani if wierzcholek not in kolejka]
            kolejka.extend(dodawani)
        except:
            pass
        odwiedzeni.append(aktualny_wierzcholek)
    return graf.czy_dwudzielny

def wczytaj_dane(plik):
    with open (plik, "r") as p:
         kraw = []
         dane = p.readlines()
         liczba_wierzcholkow, liczba_krawedzi = dane.pop(0).split()
         graf = Graf(int(liczba_wierzcholkow), int(liczba_krawedzi))
         for line in dane:
            v, w = line.split()
            graf.dodaj(int(v), int(w))
            kraw.append((v,w))
    return graf, kraw

def stworz(liczba_wierzcholkow, gestosc):
    graf = Graf(liczba_wierzcholkow, 0)
    kraw = []
    kombinacje = []
    for i in range(1, liczba_wierzcholkow):
        for j in range(i+1, liczba_wierzcholkow + 1):
            if j != i:
                kombinacje.append((i, j))
    vw = random.choice(kombinacje)
    v, w = vw
    kombinacje.remove(vw)
    polaczone = [w]
    for i in range(liczba_wierzcholkow-2):
        graf.dodaj(v, w)
        graf.dodaj(w, v)
        kraw.append((v, w))
        kraw.append((w, v))
        graf.liczba_krawedzi += 2
        for k in kombinacje:
            if v in k and w in k:
                kombinacje.remove(k)
                break
        w = v
        polaczone.append(v)
        v = random.choice(polaczone)
    liczba_krawedzi = gestosc/100*liczba_wierzcholkow*(liczba_wierzcholkow-1)
    liczba_krawedzi -= graf.liczba_krawedzi
    liczba_krawedzi = math.ceil(liczba_krawedzi/2)
    for i in range(liczba_krawedzi):
        vw = random.choice(kombinacje)
        kombinacje.remove(vw)
        kraw.append((vw[0], vw[1]))
        kraw.append((vw[1], vw[0]))
        graf.dodaj(vw[0], vw[1])
        graf.dodaj(vw[1], vw[0])
        graf.liczba_krawedzi+=2
    return graf, kraw

def stworz_graf(liczba_wierzcholkow, gestosc):
    G = nx.Graph()
    g = Graf(liczba_wierzcholkow, 4)
    for i in range(liczba_wierzcholkow):
        for j in range(i, liczba_wierzcholkow+1):
            if j != i:
                G.add_edge(i,j)
                g.dodaj(i, j)
                g.dodaj(j, i)
                print(i,j)
                if (5*round(nx.density(G)*100/5)) == gestosc:
                    return G, g
    raise Exception("Nie dopasowano grafu!")

#G = stworz_graf(10, 25)
#nx.draw(G, with_labels=True)
#G = nx.tetrahedral_graph()
#G = nx.complete_bipartite_graph(5, 10)
#G = nx.barbell_graph(5,6)
#G = nx.lollipop_graph(10, 5)
#plt.subplot(121)
#plt.subplot(122)
#nx.draw_shell(G, nlist=[range(5,10), range(5)], with_labels=True)
#print(G.get_edge_data())
#print(G.neighbors(0))
#print(G.nodes)
#print(G.number_of_edges())
#print(G.number_of_nodes())

def wyswietl_graf(krawedzie):
    G = nx.Graph()
    G.add_edges_from(krawedzie)
    nx.draw(G, with_labels=True)
    #print(nx.density(G))
    plt.show()

def wersjaA(plik):
    graf, kraw = wczytaj_dane(plik)
    algorytm_BFS(graf)
    algorytm_DFS(graf)
    wyswietl_graf(kraw)

def wersjaB():
    grafy = {}
    for i in range(10):
        for q in range(25, 101, 10):
            #g,k = stworz(10, q)
            G, g = stworz_graf(10, q)
            #wyswietl_graf(k)
            nx.draw(G, with_labels=True)
            plt.plot()
            #g.wyswietl_wierzcholki()
            if q in grafy:
                grafy[q].append(g)
            else:
                grafy[q] = [g]
    dwudzielnosc = {}
    for q, grafs in grafy.items():
        for g in grafs:
            algorytm_DFS_bez_print(g)
            if q in dwudzielnosc:
                if g.czy_dwudzielny:
                    dwudzielnosc[q][0] += 1
                else:
                    dwudzielnosc[q][1] += 1
            else:
                if g.czy_dwudzielny:
                    dwudzielnosc[q] = [1, 0]
                else:
                    dwudzielnosc[q] = [0, 1]

    print(dwudzielnosc)

#wersjaA("dane_graf3.txt")

wersjaB()
#g1, kraw= stworz(10, 30)
#g1.wyswietl_wierzcholki()
#algorytm_DFS(g1)
#print(f'Czy graf dwudzielny: {g1.czy_dwudzielny}')
