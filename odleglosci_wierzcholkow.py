def wyznaczanie_maksymalnej_odleglosci(tablica_wierzcholkow):
    max_odleglosc = 0
    przypisanie_zmiennej = 0
    porownanie = 0
    for punkt1 in tablica_wierzcholkow:
        przypisanie_zmiennej += 1
        for punkt2 in tablica_wierzcholkow:
            przypisanie_zmiennej += 1
            x1, y1 = punkt1
            x2, y2 = punkt2
            odleglosc = ((x2 - x1)**2+(y2-y1)**2)**(1/2)
            if odleglosc>max_odleglosc:
                porownanie += 1
                max_odleglosc = odleglosc
                A = punkt1
                B = punkt2
            else:
                porownanie += 1
    #print(f'Maksymalna odległość między punktami wynosi {max_odleglosc}')
    #print(f'Punkt 1: {A}, Punkt 2: {B}')
    print(f'Działania dla {len(tablica_wierzcholkow)} wierzchołków.')
    print(f'Liczba przypisań: {przypisanie_zmiennej}')
    print(f'Liczba porównań: {porownanie}')
    return max_odleglosc

def test():
    wierzcholki = [(2, 4), (4, 4), (5, 2), (3, 1), (2, 1), (1, 3)]
    if wyznaczanie_maksymalnej_odleglosci(wierzcholki) == 4.123105625617661:
        return True
print("Zdanie testu: ", test())

wyznaczanie_maksymalnej_odleglosci([(5, 5), (8, 5), (10, 4), (12 ,3), (14, 2), (12, 1), (10, 0), (8, 0), (5, 0), (2, 2)])

wyznaczanie_maksymalnej_odleglosci([(5, 5), (6, 5), (8, 5), (9, 7), (10, 4), (11, 5), (12 ,3), (13, 3), (14, 2), (13, 3),\
                                   (12, 1), (11, 1), (10, 0), (9, 1), (8, 0), (6, 0),  (5, 0), (3, 1), (2, 2), (2,4)])


