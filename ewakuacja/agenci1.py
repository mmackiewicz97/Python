import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths
import json

#ZAD_DOM:
#  - kilku z uciekinierów ma pik przed pierwszym krokiem (w lewym górnym rogu) - do naprawy
#  - pobrać wszystkie możliwe dane z eggman.json, a nie deklarować w programie na stałe

#unikanie kolizji
#instalacja biblioteki orca rv2?
#git do pobierania z githuba lub konfiguracja pycharma

class Pedestrian:
    def __init__(self, goals, velo, pre):
        self.traj = []
        self.speed = velo
        self.goals = goals
        self.pre_time = pre

    def create_vel_vector(self, actual, goal):
        vec_real = np.array(goal) - np.array(actual)  # wspolrzedne wektorow rzeczywistych aby z warunku brało goals_no
        len_vec_real = np.linalg.norm(vec_real)
        vec_u = vec_real / len_vec_real
        vec_vel = vec_u * self.speed
        return vec_vel

    def create_trajectory(self, actual, goal):
        vec_vel = self.create_vel_vector(actual, goal)

        x = actual[0] + vec_vel[0]
        y = actual[1] + vec_vel[1]
        position = (x, y)
        self.traj.append(position)
        return position, vec_vel

    def do_it(self):
        goal_no = 0
        step_no = 1
        position = (self.goals[0][0], self.goals[0][1])
        while self.pre_time-100 >= step_no:
            self.traj.append(position)
            step_no += 1

        while True:             #pętla tworząca trajektorię
            try:
                if np.linalg.norm(self.goals[goal_no] - np.array(position)) <= self.speed/2:
                    goal_no += 1
                position, vec_vel = self.create_trajectory(position, self.goals[goal_no])
            except:
                break
        #print(self.traj)
        return self.traj

    def chart(self):
        self.do_it()
        x, y = zip(*self.traj)
        plt.plot(x, y, "-o")
        plt.show()


class Pedestrians:
    def __init__(self):
        self.peds = []

    def add_pedestrians(self, ped):
        self.peds.append(ped)

    def get_trajectories(self):
        trajectories = []
        for i in self.peds:
            trajectories.append(i.do_it())
        return trajectories

    def get_chart(self):
        trajs = self.get_trajectories()
        temp_traj = []
        lens = []

        for i in trajs:
            lens.append(len(i))
        length = max(lens)
        for i in range(length):          # dla iluśtam kroków
            step = []
            for j in range(len(trajs)):  # tworzy gdzie są w danym kroku
                try:
                    step.append(trajs[j][i])
                except:
                    step.append(trajs[j][-1])
            temp_traj.append(step)          #do tego momentu tworzy odpowiednią trajektorię
        #print('trajektoria posortowana wg krokow:', temp_traj)

        foo = zip(*temp_traj)               #rysuje trajektorie
        for i in foo:
            x, y = zip(*i)
            plt.plot(x, y, "-")

        return temp_traj


class Animation:
    def __init__(self, pedest):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-1, 60), ylim=(-1, 20))
        self.n_frames = 0
        self.trial = []
        self.ang = 0
        self.create_walls()

        self.trajectory = pedest.get_chart()
        self.n_frames = len(self.trajectory)

        elipses = [mpaths.Ellipse(i, width=1, height=1, angle=self.ang) for i in
                   self.trajectory[0]]      # stworzenie kształtu i przypisanie mu cech (wymiary, współ początkowych)
        [self.trial.append(self.ax.add_patch(elipses[i])) for i in range(len(elipses))]

    def init_animation(self):
        [self.trial[i].set_visible(True) for i in range(len(self.trial))]

        return self.trial

    def animate(self, i):
        for j in range(len(self.trajectory[0])):
            self.trial[j].center = self.trajectory[i][j]
        return self.trial

    def do_animation(self, n_interval):
        animate = anim.FuncAnimation(self.fig, self.animate, frames=self.n_frames, init_func=self.init_animation,
                                     interval=n_interval, blit=True)
        plt.show()

    def create_walls(self):
        for i in obst:                                      # kreślenie ścian budynku
            corners_x = [i[0][0], i[1][0], i[2][0], i[3][0]]
            corners_y = [i[0][1], i[1][1], i[2][1], i[3][1]]
            plt.plot(corners_x, corners_y, "r", lw=3)


def change_data(eggman_ped):
    vel = eggman_ped["H_SPEED"]
    goals = []
    goals.append(eggman_ped['ORIGIN'])
    goals.extend(eggman_ped['ROADMAP'])
    pre = eggman_ped["PRE_EVACUATION"]

    return goals, vel, pre


file1 = open("egman.json", 'r')
first_floor = json.load(file1)["1"]["EVACUEES"]
file2 = open("geom.json", "r")
obst = json.load(file2)["obstacles"]["1"]


a = Pedestrians()
for i in first_floor:
    temp_ped = Pedestrian(*change_data(first_floor[i]))
    a.add_pedestrians(temp_ped)

x = Animation(a)
x.do_animation(100)