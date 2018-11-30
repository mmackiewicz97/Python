import math
warunek = 0
alfa = 0.01
h = 50
wynik = []
while warunek == 0:
    alfa+=0.01
    #h = int(math.ceil(((6*157.053/(17920*alfa))**(1/3))*100)) #cm
    b = round(alfa*h+0.5)
    q1nc = 7.914 + (b*h/10000*410*9.81*1.35/1000) #kN/m
    q1uc = 5.596 + (b*h/10000*410*9.81/1000) #kN/m
    Lef = 0.9*12.6+2*h/100 #m
    sigmacrit = 0.78*((b/100)**2)*10.2/(h/100*Lef) #GPa
    My = q1nc*(Lef**2)/8 #kNm
    lambdaa = (28/1000/sigmacrit)**(1/2)
    if lambdaa < 0.75:
        kcrit = 1
    elif lambdaa >= 0.75 and lambdaa < 1.4:
        kcrit = 1.56 - 0.75*lambdaa
    else:
        kcrit = 1/(lambdaa**2)
    Iy = b*(h**3)/12 #cm^4
    Wy = Iy/(0.5*h) #m^3
    sigmamd = My/Wy*1000 #MPa
    if h*10 >= 600:
        kh = 1
    else:
        kh =min((600/(h*10))**(1/10), 1.1)
    fmd = kh*0.8*28/1.25 #MPa
    if sigmamd <= kcrit*fmd:
        if sigmamd/(kcrit*fmd)>=0.7 and sigmamd/(kcrit*fmd)<1:
            qk = 2.663*1.2+(b*h/10000*410*9.81/1000)
            z = sigmamd / (kcrit * fmd) * 100
            if 1260/h >= 20:
                uinstG = 5/384*(qk*(12.6**4)/(12.6*1000000*Iy/100000000))*100
                uinstQ = 5/384*(2.4*(12.6**4)/(12.6*1000000*Iy/100000000))*100
                ufinG = 1.6*uinstG
                ufinQ = (1+0.3*0.6)*uinstQ
                ufin = ufinG+ufinQ
                if ufin<5.04:
                    a = ["Dane: hteoretyczne: ",int(math.ceil(((6*157.053/(17920*alfa))**(1/3))*100))," h: ", h, " b: ", b, " alfa: ", round(alfa,2), " ", round(z, 3), "% ", "pole: ", h*b]
                    wynik.append(a)
            else:
                uinstG = 5 / 384 * (qk * (12.6 ** 4) / (12.6 * 1000000 * Iy / 100000000)) * 100*(1+19.2*((h/100)/12.6)**2)
                uinstQ = 5 / 384 * (2.4 * (12.6 ** 4) / (12.6 * 1000000 * Iy / 100000000)) * 100*(1+19.2*((h/100)/12.6)**2)
                ufinG = 1.6 * uinstG
                ufinQ = (1 + 0.3 * 0.6) * uinstQ
                ufin = ufinG + ufinQ
                if ufin < 5.04:
                    a = ["Dane: hteoretyczne: ", int(math.ceil(((6 * 157.053 / (17920 * alfa)) ** (1 / 3)) * 100))," h: ", h, " b: ", b, " alfa: ", round(alfa, 2), " ", round(z, 3), "% ", "pole: ", h * b]
                    wynik.append(a)

    if alfa > 1:
        alfa = 0.01
        h+=1
    if h >100:
        break
wynik.sort(key= lambda x: x[9])
wynik.reverse()
for x in wynik:
    print(x)

