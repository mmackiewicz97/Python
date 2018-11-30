import json
import numpy.random as random
from scipy.spatial import distance
import numpy.linalg
import matplotlib.pyplot as plt

with open('egman.json') as json_data:
    data = json.load(json_data)
    dat = data['1']["EVACUEES"]
v_distance = 12

class Evacue:

    def __init__(self, preevacuation, hspeed, vspeed, originx, originy):
        self.preevacuation = preevacuation
        self.hspeed = hspeed
        self.vspeed = vspeed
        self.hdistance = random.uniform(10, 80, 1)
        self.time = self.preevacuation + v_distance/self.vspeed + self.hdistance/self.hspeed
        self.originx = originx
        self.originy = originy


class Evacuees:
    def __init__(self, tab):
        self.evacuees = tab
    def add_evacues(self, evacues):
        self.evacues = evacues
    def getevacuationtime(self):
        self.time = []
        for i in self.evacuees:
            self.time.append(i.time)

        return max(self.time)
    def getlagger(self, x):
        evacuesid = self.time.index(x)
        return evacuesid
evacues = []
i = 0
for a, b in data['1']["EVACUEES"].items():
    preevacuation = data['1']["EVACUEES"][a]["PRE_EVACUATION"]
    hspeed = data['1']["EVACUEES"][a]["H_SPEED"]
    vspeed = data['1']["EVACUEES"][a]["V_SPEED"]
    originx = data['1']["EVACUEES"][a]["ORIGIN"][0]
    originy = data['1']["EVACUEES"][a]["ORIGIN"][1]
    evacues.append(Evacue(preevacuation, hspeed, vspeed, originx, originy))
    i += 1
all = Evacuees(evacues)
lagger = float(all.getevacuationtime())
name = all.getlagger(lagger)
print("ostatni był E{} z {}s czasem".format(name, lagger))

a = (1,2,3)
b = (4,5,6)
dst = distance.euclidean(a, b)
print(dst)

points = []

for i in dat.keys():
    punkty = []
    points.insert(0, dat[i]['ORIGIN'])
    points.append(dat[i]['ROADMAP'])
    punkty.append(dat[i]['ORIGIN'])
    for n in dat[i]['ROADMAP']:
        punkty.append(n)
    plt.plot(dat[i]['ORIGIN'][0],dat[i]['ORIGIN'][1], 'o')
    plt.text(dat[i]['ORIGIN'][0],dat[i]['ORIGIN'][1], i)
    x, y = zip(*punkty)
    plt.plot(x, y, linewidth=2)
    #color="r"

plt.show()