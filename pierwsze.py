def nLiczby(nLiczbaOd, nLiczbaDo):
    nLista = []
    for i in range(nLiczbaOd, nLiczbaDo):
        for x in range(2,i):
            if (i % x) == 0:
                break
        else:
            nLista.append(i)
    suma = 0
    for i in nLista:
        suma+=i
    print('Ilosc liczb pierwszych: ',len(nLista))
    print('Suma: ', suma)
    x = 0
    for i in nLista:
        x+=1
        print(i, end=' ')
        if x%10==0:
            print(' ')
nLiczby(2,547)
#suma stu liczb pierwszych
