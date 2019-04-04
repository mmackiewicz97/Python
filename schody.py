import numpy.random as random# {{{
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths# }}}
# 2 z góry, 1 z boku
# z parteru schodzi 1osoba/sekunde, definiuje schodzenie pozostałych, kolejkowanie od dołu
# szywno wolne miejsca na piętrach
# schodzą po tablicy
# 10m/0,3cm na człowieka = 33osoby zmieszczą się na klatce 3 piętrowej
# jeden w jedną komórkę
# 1/3 z boku, 2/3 z góry, łączenie 
#losowanie random, wylosuje to wchodzi
#podwójna kolejka
#wizualizacja wysokości z, 
floor_space = 3# {{{
liczba_agentow = 3
liczba_krokow = 1
czas_interwalu = 900
area_of_people = 0.5
area_of_staircase = 9# }}}

class Queue:

    def __init__(self):
        self.queue = list()
#        self.maxSize = 8
        self.head = 0
#        self.tail = 0

    def add(self,data):
#        if self.size() >= self.maxSize:
#            return ("Queue Full")
        self.queue.extend(data)
#        self.tail += 1
        return True     

    def pop(self):
#        if self.size() <= 0:
#            self.resetQueue()
#            return ("Queue Empty") 
        data = self.queue[self.head]
        self.head+=1
        return data

    def all(self):
        return self.queue

    def que(self):
        return self.queue[self.head:]
                
    def size(self):
        return len(self.queue) - self.head
    
    def resetQueue(self):
#        self.tail = 0
        self.head = 0
        self.queue = list()
#a = Queue()
#for i in range(5):
#    a.add("st"+str(i))
#print(a.all())
#print(a.que())
#print(a.size())
#print(a.pop())
#print(a.all())
#print(a.que())
#print(a.size())

class Agent:# {{{

    def __init__(self):
        self.name = ""
        floor = [0, 3, 6, 9, 12]
        self.position = (0.5, floor[random.randint(0, 5)])
        self.outside = 0

    def __str__(self):
        return self.name

    def if_in(self):
        return random.randint(0,3)# }}}

class Pedestrians:

    def __init__(self):
        self.agent = []
        self.QUEUE = Queue()
        for i, z in enumerate('abcdefghijklmnoprst'):
            x = Agent()
            x.position = (i/30, x.position[1])
            x.name = i
            self.agent.append(x)                
        self.traj = []
        x = [None]*3
        self.que = {0:x,1:x,2:x,3:x,4:x}
        self.floorque = {}
        #self.add_agent()
        self.do_traj()
    def add_agent(self):
        for i in range(liczba_agentow):
            self.agent.append(Agent())
    def do_traj(self):
        for agent in self.agent:
            pietro = math.floor(agent.position[1]/3)
            if pietro in self.floorque:
                if agent not in self.floorque[pietro]:
                    self.floorque[pietro].append(agent)
            else:
                self.floorque[pietro]=[agent]
        for floor in self.floorque.keys():
            self.floorque[floor].sort(key=lambda x: x.position[0])
        for i in range(liczba_krokow):
            for k,v in self.que.items():
                if self.que[k][1] != None:
                    if self.floorque[k][0].if_in():
                        self.que[k][0] = self.floorque[k].pop(0)
                else:
                    self.que[k][0] = self.floorque[k].pop(0)
                self.QUEUE.add(v)
        for x, i in enumerate(self.QUEUE.que()):
            try:
                i.position = (i.position[0], x)
            except:
                pass
        self.QUEUE.pop().position = (0, 0)
        k = 0
        self.que = {}
        for x, i in enumerate(self.QUEUE.que()):
            if x%3==0:
                k+=1
            self.que[k]

# 
        

#                for x in range(len(self.floorque[pietro])):
#                    self.floorque[pietro][x].position=(1, pietro*3+x)
#            out = self.floorque[0].pop(0)
#            out.position = (4.2, i/2)
#            out.outside = 1
#            traj = []
#            for agent in self.agent:
#                traj.append(agent.position)
#            #    print(agent.name, agent.position)
#            self.traj.append(traj)
#            if len(self.floorque[0])<1:
#                print("zakonczono w: ", i, " krokach")
#                break

A = Pedestrians()
class Animation:# {{{

    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 5), ylim=(0, 15.1))
        self.trial = []
        self.trajectory = A.traj
        self.n_frames = len(self.trajectory)
        color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        elipses = [mpaths.Ellipse(i, width=0.1, height=1, angle=0, color=color[random.randint(0, 7)]) for i in self.trajectory[0]]
        [self.trial.append(self.ax.add_patch(elipses[i])) for i in range(len(elipses))]
        plt.plot((0.9,0.9,4.1,4.1),(0,15,15,0), "r", lw=2)
        plt.plot((0.9, 4.1), (3,3), "y", lw = 2)
        plt.plot((0.9, 4.1), (6,6), "y", lw = 2)
        plt.plot((0.9, 4.1), (9,9), "y", lw = 2)
        plt.plot((0.9, 4.1), (12,12), "y", lw = 2)

    def init_animation(self):
        [self.trial[i].set_visible(True) for i in range(len(self.trial))]
        return self.trial

    def animate(self, i):
        for j in range(len(self.trajectory[0])):
            self.trial[j].center = self.trajectory[i][j]
        return self.trial

    def do_animation(self, n_interval):
        animate = anim.FuncAnimation(self.fig, self.animate, frames=self.n_frames, init_func=self.init_animation, interval=n_interval, blit=True)
        plt.show()# }}}
#Animation().do_animation(czas_interwalu)
