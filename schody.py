import numpy.random as random# {{{
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths# }}}
# sprawdzenie czy może wejść, czy gęstość nie jest większa niż powierzchnia klatki{{{
# jak nie ma to czeka na wejście
# 2 z góry, 1 z boku
# z parteru schodzi 1osoba/sekunde, definiuje schodzenie pozostałych, kolejkowanie od dołu
# parter powierzchnia spocznika, I piętro schody+spocznik
# kolejka, fifo, po dwóch do drzwi
# po biegach chodzą po dwóch, w drzwiach pojedynczo
# szywno wolne miejsca na piętrach
# schodzą po tablicy
# 10m/0,3cm na człowieka = 33osoby zmieszczą się na klatce 3 piętrowej
# jeden w jedną komórkę

liczba_agentow = 100
liczba_krokow = 150
czas_interwalu = 50
area_of_people = 0.5
area_of_staircase = 9# }}}

# 1/3 z boku, 2/3 z góry, łączenie 
# prawdziwa klatka, wchodzą z jednej strony

class Agent:

    def __init__(self):
        self.speed = random.normal(1.2, 0.2, 1)
        floor = [3, 6, 9, 12]
        self.position = (random.randint(1, 50)/10, floor[random.randint(0, 4)])
    def get_trajectory(self):
        if self.position[0] < 1:
            x = self.position[0]+(self.speed/80)
            y = self.position[1]
            self.position = (x, y)
        elif self.position[0] > 4:
            x = self.position[0]-(self.speed/80)
            y = self.position[1]
            self.position = (x, y)
        else:
            x = self.position[0]
            y = self.position[1]-(self.speed/10)
            self.position = (x, y)
        return float(x), float(y)
    def set_speed(self, ro):
        self.speed =(-262.23776224*ro**4+517.09401709*ro**3-273.42657343*ro**2-25.794483294*ro+48.531468531)/20

class Pedestrians:

    def __init__(self):
        self.agent = []
        self.traj = []
        self.add_agent()
        self.do_traj()
    def add_agent(self):
        for i in range(liczba_agentow):
            self.agent.append(Agent())
    def do_traj(self):
        for x in range(liczba_krokow):
            traj = []
            count_floor = {}
            ro = {}
            for agent in self.agent:
                position = agent.get_trajectory()
                traj.append(position)
                count_floor[math.floor(position[1]/3)]=count_floor.get(math.floor(position[1]/3), 0)+1
                ro[math.floor(position[1]/3)]=count_floor[math.floor(position[1]/3)]*area_of_people/area_of_staircase
                if ro[math.floor(position[1]/3)] < 1:
                    agent.set_speed(ro[math.floor(agent.position[1]/3)])
                else:
                    agent.set_speed(1.04848953)
            self.traj.append(traj)
            #print(traj)
            #print(self.traj)
            
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
Animation().do_animation(czas_interwalu)
