import random
g = 1
bad = []
good = []
try:
    while True:
        if len(good) == 100:
            print("Przeszedłeś całą tabliczkę! Wciśnij CTRL+C by powtórzyć nietrafione.")
            break
        X = random.randint(1,10)
        Y = random.randint(1,10)
        if (X,Y) in good:
            X = random.randint(1,10)
            Y = random.randint(1,10)
            continue
        print(X, "*", Y,"= ")
        Z = int(input())
        if X*Y==Z:
            print(X,"*",Y,"= ",Z, "Za pierwszym ", g," raz!")
            good.append((X,Y))
            g+=1
        else:
            x = 0
            while X*Y != Z:
                x+=1
                if x >2:
                    bad.append((X,Y))
                print("Spróbuj jeszcze raz")
                print(X, "*", Y,"= ")
                Z = int(input())
            print(X,"*",Y,"= ",Z, "Dobrze")
            good.append((X,Y))
    input()
except KeyboardInterrupt:
    print("Powtórka")
    while True:
        X,Y=random.choice(bad)
        print(X, "*", Y,"= ")
        Z = int(input())
        if X*Y==Z:
            print(X,"*",Y,"= ",Z)
        else:
            while X*Y != Z:
                print("Spróbuj jeszcze raz")
                print(X, "*", Y,"= ")
                Z = int(input())
            print(X,"*",Y,"= ",Z, "Dobrze")
        bad.remove((X,Y))
        if len(bad) ==0:
            print("Zakończono")
            print("Dobra robota :D")
            break
        print("Została: ", len(bad), " para liczb")
