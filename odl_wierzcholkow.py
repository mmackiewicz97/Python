import math
def wyznaczanie_maksymalnej_odleglosci(tablica_wierzcholkow):
    max_odleglosc = 0
    przypisanie_zmiennej = 0
    porownanie = 0
    tablica = []
    for i in range(len(tablica_wierzcholkow)):
        przypisanie_zmiennej += 1
        if i < (len(tablica_wierzcholkow) - 1):
            x1, y1 = tablica_wierzcholkow[i]
            x2, y2 = tablica_wierzcholkow[i+1]
        else:
            x1, y1 = tablica_wierzcholkow[-1]
            x2, y2 = tablica_wierzcholkow[0]

        if (x2-x1) != 0:
            a = (y2-y1)/(x2-x1)
        else:
            a = 0
        b = y1 - a*x1
        tablica.append((a, b, (x1, y1), (x2, y2)))
    a1, b1, punkt1, punkt2 = tablica.pop(0)
    tablica.sort(key=lambda x: x[0])
    temp = []
    for punkt in tablica_wierzcholkow[2:]:
        if a1 != 0:
            b = a1*punkt[0]-punkt[1]
            temp.append((punkt, b))
        else:
            odleglosc = math.fabs(punkt1[1] - punkt[1])
            temp.append((punkt, odleglosc))
    if a1 == 0:
        temp.sort(key=lambda x: x[1], reverse=True)
    else:
        temp.sort(key=lambda x: x[1])
    print(temp)
    #        odleglosc = ((x2 - x1)**2+(y2-y1)**2)**(1/2)
    #        if odleglosc>max_odleglosc:
    #            porownanie += 1
    #            max_odleglosc = odleglosc
    #            A = punkt1
    #            B = punkt2
    #        else:
    #            porownanie += 1
    ##print(f'Maksymalna odległość między punktami wynosi {max_odleglosc}')
    ##print(f'Punkt 1: {A}, Punkt 2: {B}')
    #print(f'Działania dla {len(tablica_wierzcholkow)} wierzchołków.')
    #print(f'Liczba przypisań: {przypisanie_zmiennej}')
    #print(f'Liczba porównań: {porownanie}')
    #return max_odleglosc

def test():
    wierzcholki = [(2, 4), (4, 4), (5, 2), (3, 1), (2, 1), (1, 3)]
    if wyznaczanie_maksymalnej_odleglosci(wierzcholki) == 4.123105625617661:
        return True
#print("Zdanie testu: ", test())
wyznaczanie_maksymalnej_odleglosci([(2, 4), (4, 4), (5, 2), (3, 1), (2, 1), (1, 3)])
#wyznaczanie_maksymalnej_odleglosci([(5, 5), (8, 5), (10, 4), (12 ,3), (14, 2), (12, 1), (10, 0), (8, 0), (5, 0), (2, 2)])

#wyznaczanie_maksymalnej_odleglosci([(5, 5), (6, 5), (8, 5), (9, 7), (10, 4), (11, 5), (12 ,3), (13, 3), (14, 2), (13, 3),\
                                   #(12, 1), (11, 1), (10, 0), (9, 1), (8, 0), (6, 0),  (5, 0), (3, 1), (2, 2), (2,4)])


