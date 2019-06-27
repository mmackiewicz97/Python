import os
#    if filename.endswith('.txt'):
#        with open(os.path.join('/home/mateusz/Pulpit/k', filename), "w") as f:
#            f.write("jakiś, tekst")
#            f.writelines(dana[0]+"- "+dana[1]+" "+dana[2] for dana in dan)
#with open(os.path.join('/home/mateusz/Pulpit/k', filename), "r") as f:
#    print(f.read())
#    a = f.read()
path = os.getcwd()
#print(path)
try:
    os.mkdir("zdjecia")
except FileExistsError:
    pass
#os.makedirs("zdj/1/2")

#os.chdir("zdjecia")

#for i in range(10):
#    f=open("IMG_"+str(i)+".jpg", "w+")
#    f.close()

#for filename in os.listdir(os.getcwd()):
#    os.remove(filename)

a = []
for filename in os.listdir("zdjecia"):
    a.append(filename)
b = []
for filename in os.listdir("zdjecia2"):
    b.append(filename)
a = set(a)
b = set(b)
directory = os.getcwd()+"/zdjecia"
directory2 = os.getcwd()+"/zdjecia2"
for file in a-b:
    path = os.path.join(directory, file)
    target = os.path.join(directory2, file)
    os.rename(path, target)
#for file in a|b:
#    path = os.path.join(directory, file)
#    target = os.path.join(directory2, file)
#    os.rename(path, target)
#for file in b-a:
#    print(file)
#    path = os.path.join(directory, file)
#    target = os.path.join(directory2, file)
#    os.rename(path, target)
