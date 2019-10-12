import os
import sys
import hashlib
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
print(findDup("C:\\Users\\Mateusz\\Desktop\\test"))
def joindict(dict1, dict2):
    
#    if filename.endswith('.txt'):
#        with open(os.path.join('/home/mateusz/Pulpit/k', filename), "w") as f:
#            f.write("jakiś, tekst")
#            f.writelines(dana[0]+"- "+dana[1]+" "+dana[2] for dana in dan)
#with open(os.path.join('/home/mateusz/Pulpit/k', filename), "r") as f:
#    print(f.read())
#    a = f.read()
#path = os.getcwd()
#print(path)
#try:
#    os.mkdir("zdjecia")
#except FileExistsError:
#    pass
#os.makedirs("zdj/1/2")

#os.chdir("zdjecia")

#for i in range(10):
#    f=open("IMG_"+str(i)+".jpg", "w+")
#    f.close()

#for filename in os.listdir(os.getcwd()):
#    os.remove(filename)

#a = []
#for filename in os.listdir("zdjecia"):
#    a.append(filename)
#b = []
#for filename in os.listdir("zdjecia2"):
#    b.append(filename)
#a = set(a)
#b = set(b)
#directory = os.getcwd()+"/zdjecia"
#directory2 = os.getcwd()+"/zdjecia2"
#for file in a-b:
#    path = os.path.join(directory, file)
#    target = os.path.join(directory2, file)
#    os.rename(path, target)
#for file in a|b:
#    path = os.path.join(directory, file)
#    target = os.path.join(directory2, file)
#    os.rename(path, target)
#for file in b-a:
#    print(file)
#    path = os.path.join(directory, file)
#    target = os.path.join(directory2, file)
#    os.rename(path, target)
