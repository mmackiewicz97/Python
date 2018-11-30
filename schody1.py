import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths
liczba_agentow = 20
liczba_krokow = 100
czas_interwalu = 30
class Agent:

    def __init__(self):
        self.speed = random.normal(1.2, 0.2, 1)
        self.position = (random.randint(10, 40)/10, random.randint(20, 150)/10)
    def get_trajectory(self):
        x = self.position[0]
        y = self.position[1]-(self.speed/8)
        self.position = (x, y)
        return x, float(y)

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
            for i in self.agent:
                traj.append(i.get_trajectory())
            self.traj.append(traj)

class Animation:

    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 5), ylim=(0, 17))
        self.trial = []
        self.trajectory = Pedestrians().traj
        self.n_frames = len(self.trajectory)
        color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        elipses = [mpaths.Ellipse(i, width=0.1, height=1, angle=0, color=color[random.randint(0, 7)]) for i in self.trajectory[0]]
        [self.trial.append(self.ax.add_patch(elipses[i])) for i in range(len(elipses))]
        plt.plot((0.9,0.9,4.1,4.1),(0,15,15,0), "r", lw=2)

    def init_animation(self):
        [self.trial[i].set_visible(True) for i in range(len(self.trial))]
        return self.trial

    def animate(self, i):
        for j in range(len(self.trajectory[0])):
            self.trial[j].center = self.trajectory[i][j]
        return self.trial

    def do_animation(self, n_interval):
        animate = anim.FuncAnimation(self.fig, self.animate, frames=self.n_frames, init_func=self.init_animation, interval=n_interval, blit=True)
        plt.show()
Animation().do_animation(czas_interwalu)