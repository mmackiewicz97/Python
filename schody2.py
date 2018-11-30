import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths
#gęstość na piętrze
#różna prędkość w zależności od gęstości

#10 strona książki człowiek 0,5 m^2
liczba_agentow = 20
liczba_krokow = 100
czas_interwalu = 50
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
            return float(x), float(y)
        elif self.position[0] > 4:
            x = self.position[0]-(self.speed/80)
            y = self.position[1]
            self.position = (x, y)
            return float(x), float(y)
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
            a1 = 0
            a2 = 0
            a3 = 0
            a4 = 0
            traj = []
            for i in self.agent:
                traj.append(i.get_trajectory())
            for i in traj:
                if i[1] <= 3:
                    a1 +=1
                elif i[1] >3 and i[1]<=6:
                    a2 +=1
                elif i[1] >6 and i[1]<=9:
                    a3 +=1
                elif i[1] >9 and i[1]<=12:
                    a4 +=1
            for i in self.agent:
                if i.position[0] > 1 and i.position[0] < 4:
                    if float(i.position[1]) <=3:
                        i.set_speed(a1*0.4/9)
                    elif float(i.position[1])>3 and float(i.position[1])<=6:
                        i.set_speed(a2*0.4/9)
                    elif float(i.position[1])>6 and float(i.position[1])<=9:
                        i.set_speed(a3*0.4/9)
                    elif float(i.position[1])>9 and float(i.position[1])<=12:
                        i.set_speed(a4*0.4/9)
            #print(x, a1*0.4/9, a2*0.4/9, a3*0.4/9, a4*0.4/9) #ilość osób na danym piętrze * powierzchnia osoby / powierzchnia piętra
            self.traj.append(traj)
A = Pedestrians()

class Animation:

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
        plt.show()
Animation().do_animation(czas_interwalu)
