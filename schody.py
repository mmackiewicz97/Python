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
floor_space = 1# {{{
liczba_agentow = 3
liczba_krokow = 9
czas_interwalu = 50
area_of_people = 0.5
area_of_staircase = 9# }}}
class Agent:# {{{

    def __init__(self):
        self.name = ''
        floor = [0, 3, 6, 9, 12]
        self.position = (0.5, floor[random.randint(0, 5)])# }}}
a, b, c, d, e = Agent(),  Agent(), Agent(), Agent(), Agent()# {{{
a.position = (0.5,0)
b.position = (0.5,1)
c.position = (0.5,2)
d.position = (0.5,3)
e.position = (0.5,6)
a.name = "a"
b.name = "b"
c.name = "c"
d.name = "d"
e.name = "e" #}}}
#zmienna zdefiniowana w init, nie da się odwołać do niej w innej metodzie ale A.zmienna istnieje
class Pedestrians:

    def __init__(self):
        self.agent = [b, a, c, d,e]
        self.traj = []
        #self.add_agent()
        self.loop()
    def add_agent(self):
        for i in range(liczba_agentow):
            self.agent.append(Agent())
    def do_traj(self):
        traj = []
        x = 0
        for agent in self.agent:
            pietro = math.floor(agent.position[1]/3)
            try:
                if agent not in self.floorque[pietro]:
                    print('nie w kolejce', agent.name)
                    try:
                        while len(self.floorque[pietro]) <= floor_space:
                            x+=1
                            if x%3==0:
                                x = 0
                                self.floorque[pietro].append(agent)
                                break
                            else:
                                try:
                                    self.floorque[pietro].append(self.floorque[pietro+1].pop(0))
                                except KeyError:
                                    pass
                    except:
                        pass
            except:
                self.floorque[pietro]=[agent]
        for key in self.floorque.keys():
            self.floorque[key].sort(key=lambda x: x.position[1])
            for i in range(len(self.floorque[key])):
                self.floorque[key][i].position=(1, key+i/10)
                print(self.floorque[key], key)
        for agent in self.agent:
            traj.append(agent.position)
        self.floorque[0][0].position = (0, 0)
        self.floorque[0].pop(0)
        self.agent.remove(self.floorque[0][0])
        return traj
    def loop(self):
        self.floorque = {}
        for i in range(4):
            self.traj.append(self.do_traj())
A = Pedestrians()
#print(A.x)
#print(dir(A))
for i in A.traj:
    print(i)
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
