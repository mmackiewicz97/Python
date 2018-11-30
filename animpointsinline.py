import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths
class Pedestrian:
    def __init__(self, goals, velo):
        self.traj = []
        self.start = (0, 0)
        self.speed = velo
        self.traj.append(self.start)
        self.goals = goals

    def create_vel_vector(self, actual, goal):
        vec_real = np.array(goal) - np.array(actual)
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
        position, vec_vel = self.create_trajectory(self.start, self.goals[goal_no])

        i = 0
        while i == 0:
            try:
                if np.linalg.norm(self.goals[goal_no] - np.array(position)) <= self.speed:
                    goal_no += 1
                position, vec_vel = self.create_trajectory(position, self.goals[goal_no])

            except:
                break

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
        self.peds.extend(ped)
        print(self.peds)

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
        length = min(lens)
        for i in range(length):
            step = []
            for j in range(len(trajs)):
                step.append(trajs[j][i])
            temp_traj.append(step)
        print(temp_traj)

        foo = zip(*temp_traj)
        for i in foo:
            x, y = zip(*i)
            plt.plot(x, y, "-")

        return temp_traj


class Animation:
    def __init__(self, pedest):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
        self.n_frames = 0
        self.trial = []
        self.ang = 0

        self.trajectory = pedest.get_chart()
        self.n_frames = len(self.trajectory)

        elipses = [mpaths.Ellipse(i, width=5, height=5, angle=self.ang) for i in self.trajectory[0]]
        [self.trial.append(self.ax.add_patch(elipses[i])) for i in range(len(elipses))]

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


d = Pedestrian([(10, 10), (60, 30), (9, 12)], 2)
e = Pedestrian([(8, 11), (-5, 39), (18, 72)], 1)
f = Pedestrian([(-5, -34), (30, 67), (-40, 97)], 2)
g = Pedestrian([(-25, 12), (-15, -8), (6, 9)], 1)
h = Pedestrian([(-70, 10), (-30, -50), (40, 99)], 3)
peds = [d, e, f, g, h]
a = Pedestrians()
a.add_pedestrians(peds)

x = Animation(a)
x.do_animation(100)