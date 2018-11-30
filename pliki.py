import os
dan=[["jeden", '1', '3']]
for filename in os.listdir('/home/mateusz/Pulpit/k'):
    print(filename)
    if filename.endswith('.txt'):
        with open(os.path.join('/home/mateusz/Pulpit/k', filename), "w") as f:
            f.write("jakiś, tekst")
            f.writelines(dana[0]+"- "+dana[1]+" "+dana[2] for dana in dan)
with open(os.path.join('/home/mateusz/Pulpit/k', filename), "r") as f:
    print(f.read())
    a = f.read()