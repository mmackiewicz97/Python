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
floor_space = 2# {{{
liczba_agentow = 3
liczba_krokow = 15
czas_interwalu = 50
area_of_people = 0.5
area_of_staircase = 9# }}}
class Agent:# {{{

    def __init__(self):
        self.name = ""
        floor = [0, 3, 6, 9, 12]
        self.position = (0.5, floor[random.randint(0, 5)])
        self.outside = 0# }}}
        if_tab = [0,0,1]
        self.if_in = if_tab[random.randint(0,3)]

class Pedestrians:

    def __init__(self):
        y = 0 
        self.agent = []
        for i in 'abcdefg':
            x = Agent()
            x.position = (0.5, 0+y)
            y+=1
            x.name = i
            self.agent.append(x)                

        self.traj = []
        self.floorque = {}
        #self.add_agent()
        self.do_traj()
    def add_agent(self):
        for i in range(liczba_agentow):
            self.agent.append(Agent())
    def do_traj(self):
        for i in range(liczba_krokow):
            for agent in self.agent:
                pietro = math.floor(agent.position[1]/3)
                if agent.outside == 0:
                    if agent.position[0] >= 1:
                        if pietro in self.floorque:
                            if agent not in self.floorque[pietro]:
                                self.floorque[pietro].append(agent)
                        else:
                            self.floorque[pietro]=[agent]
                    else:
                        if pietro in self.floorque:
                            if len(self.floorque[pietro]) < floor_space:
                                try:
                                    new = self.floorque[pietro+1].pop(0)
                                    new.position = (1, pietro*3)
                                    self.floorque[pietro].append(new)
                                    if len(self.floorque[pietro]) < floor_space:
                                        try:
                                            new = self.floorque[pietro+1].pop(0)
                                            new.position = (1, pietro*3)
                                            self.floorque[pietro].append(agent)
                                            agent.position = (1, agent.position[1])
                                            self.floorque[pietro].append(new)
                                        except:
                                            self.floorque[pietro].append(agent)
                                            agent.position = (1, agent.position[1])
                                except:
                                    self.floorque[pietro].append(agent)
                                    agent.position = (1, agent.position[1])
                        else:
                            self.floorque[pietro]=[agent]
                            agent.position = (1, agent.position[1])
            print("krok: ", i)
            for floor in self.floorque.keys():
                #self.floorque[floor].sort(key=lambda x: x.position[1])
                if len(self.floorque[floor]) < floor_space:
                    try:
                        self.floorque[floor].append(self.floorque[floor+1].pop(0))
                    except:
                        pass
                print(floor,": {}".format([agent.name for agent in self.floorque[floor]]))
            print("\n")
            #for i in range(len(self.floorque[key])):
             #       self.floorque[key][i].position=(1, key+i/10)
            if len(self.floorque[0])<1:
                print("zakonczono w: ", i, " krokach")
                break
            out = self.floorque[0].pop(0)
            out.position = (0, 0)
            out.outside = 1
            traj = []
            for agent in self.agent:
                traj.append(agent.position)
        self.traj.append(traj)

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
