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
    def ustaw_kolor(self, v, kolor):
        for x in self.wierzcholki:
            if x.numer == v:
                if x.kolor:
                    if x.kolor != kolor:
                        print(f'Graf niedwudzielny!  Wierzchołek: {x.numer} ma ustawiony kolor {x.kolor}. Próbujesz zmienić na {kolor}.')
                        self.czy_dwudzielny = False
                else:
                    print(f'Ustawiam kolor wierzcholka {x.numer} na kolor {kolor}')
                    x.kolor = kolor

class Wierzcholek:
    def __init__(self, numer):
        self.numer = numer
        self.sasiedzi = []
        self.kolor = None
    def __repr__(self):
        return f'Wierzchołek: {self.numer} - sąsiedzi: {"".join(map(str,self.sasiedzi))}'
    def zwroc_kolor(self):
        return f'Wierzchołek: {self.numer} - kolor: {self.kolor}'

def algorytm_BFS(graf):
    print("/"*10+" ALGORYTM BFS "+"\\"*10)
    print("")
    graf.wyswietl_wierzcholki()
    odwiedzeni = []
    graf.ustaw_kolor(1, KOLOR[1])
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
                graf.ustaw_kolor(wierzcholek, KOLOR[(nrkoloru+1)%2])
            dodawani = [wierzcholek for wierzcholek in dodawani if wierzcholek not in kolejka]
            kolejka.extend(dodawani)
        except:
            pass
        odwiedzeni.append(aktualny_wierzcholek)
        print(f'Odwiedzone: {"".join(map(str, odwiedzeni))}, na stosie: {"".join(map(str, kolejka))}')

def algorytm_DFS(graf):
    print("/"*10+" ALGORYTM DFS "+"\\"*10)
    print("")
    graf.wyswietl_wierzcholki()
    odwiedzeni = []
    graf.ustaw_kolor(1, KOLOR[1])
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
                graf.ustaw_kolor(wierzcholek, KOLOR[(nrkoloru+1)%2])
            dodawani = [wierzcholek for wierzcholek in dodawani if wierzcholek not in kolejka]
            kolejka.extend(dodawani)
        except:
            pass
        odwiedzeni.append(aktualny_wierzcholek)
        print(f'Odwiedzone: {"".join(map(str, odwiedzeni))}, na stosie: {"".join(map(str, kolejka))}')

def wczytaj_dane(plik):
    with open (plik, "r") as p:
         dane = p.readlines()
         liczba_wierzcholkow, liczba_krawedzi = dane.pop(0).split()
         graf = Graf(int(liczba_wierzcholkow), int(liczba_krawedzi))
         for line in dane:
            v, w = line.split()
            graf.dodaj(int(v), int(w))
    return graf

# graf = wczytaj_dane("dane_graf.txt")
# algorytm_BFS(graf)
# print("")
# algorytm_DFS(graf)
# print("")
# print(f'Czy graf dwudzielny: {graf.czy_dwudzielny}')
# print("")
# graf.wyswietl_kolor()

def stworz(liczba_wierzcholkow, gestosc):
    graf = Graf(liczba_wierzcholkow, 0)
    kraw = []
    for k in range(1, liczba_wierzcholkow):
        graf.dodaj(k, k+1)
        graf.dodaj(k+1, k)
        kraw.append((k, k+1))
        kraw.append((k+1, k))
        graf.liczba_krawedzi += 2
    graf.dodaj(liczba_wierzcholkow, 1)
    kraw.append((liczba_wierzcholkow, 1))
    graf.liczba_krawedzi += 1
    qmin = 5 * round(graf.liczba_krawedzi / (liczba_wierzcholkow * (liczba_wierzcholkow - 1)) * 100 / 5)
    for i in range(1, liczba_wierzcholkow):
        for j in range(i+2, liczba_wierzcholkow + 1):
            if j != i:
                graf.dodaj(i, j)
                kraw.append((i, j))
                if i == 1 and j == liczba_wierzcholkow:
                    pass
                else:
                    kraw.append((j, i))
                    graf.dodaj(j, i)
                q = 5*round(graf.liczba_krawedzi/(liczba_wierzcholkow*(liczba_wierzcholkow-1))*100/5)
                if q == gestosc:
                    return graf, kraw
                graf.liczba_krawedzi += 2
    #raise Exception(f'Podano zbyt małą gęstość grafu - {gestosc}! Minimalna wartość wynosi: {qmin}')
g1, kraw= stworz(10, 100)
grafy = {}
for i in range(2):
    for q in range(20, 105, 5):
        g,k = stworz(10, q)
        if q in grafy:
            grafy[q].append(g)
        else:
            grafy[q] = [g]
print(grafy)
dwudzielnosc = {}
for q, grafs in grafy.items():
    for g in grafs:
        algorytm_DFS(g)
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



#algorytm_BFS(g1)
print("")
#algorytm_DFS(g1)
print("")
print(f'Czy graf dwudzielny: {g1.czy_dwudzielny}')
print("")
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from(range(1,10))
G.add_edges_from(kraw)
nx.draw(G, with_labels=True)
plt.show()
#g1.wyswietl_kolor()

def stworz_graf(liczba_wierzcholkow, gestosc):
    print("Minimalna gęstość grafu wynosi: ", nx.density(G)*100)
    for i in range(liczba_wierzcholkow):
        for j in range(i, liczba_wierzcholkow+1):
            if j != i:
                G.add_edge(i,j)
                if (5*round(nx.density(G)*100/5)) == gestosc:
                    print(nx.density(G)*100)
    return G
    #raise Exception


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
