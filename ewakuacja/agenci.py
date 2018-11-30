import numpy as np
import rvo2
import matplotlib.pyplot as plt
import json
import matplotlib.animation as anim
from matplotlib import patches as mpaths

sim = rvo2.PyRVOSimulator(0.05, 0.8, 5, 1, 0.05, 0.3, 2)

# orderedDict
#jeżeli nie widzi celu idzie kawałek dalej

class Agent:

    def __init__(self, goals, pretime, speed, position):
        self.agent = sim.addAgent(position)
        self.speed = speed
        sim.setAgentMaxSpeed(self.agent, speed)
        self.goals = goals
        self.current_goal = 0
        self.pretime = pretime
        self.velocity = [(1,1)]

    def get_position(self):
        return sim.getAgentPosition(self.agent)

    def set_velocity(self, goal):
        velocity_real = np.array(goal) - np.array(sim.getAgentPosition(self.agent))
        len_velocity_real = np.linalg.norm(velocity_real)
        velocity = (velocity_real / len_velocity_real) * self.speed # normalizacja wektora(jednostkowy) * prędkość=kierunek i prędkość
        self.velocity.append(tuple(velocity))
        sim.setAgentPrefVelocity(self.agent, tuple(velocity))

    def step(self):

        # if sim.getGlobalTime() >= self.pretime: działa, długo trzeba czekać
            if (np.linalg.norm(self.goals[self.current_goal] - np.array(self.get_position())) <= 0.7) and (self.current_goal < len(self.goals)-1):
                if sim.queryVisibility(self.get_position(), tuple(self.goals[self.current_goal+1]), radius=0.3):  # odległość dzieląca agenta od drzwi
                    self.current_goal += 1
                    # if self.current_goal >= len(self.goals): #idą z ostatnim wektorem
                    #     self.current_goal = 0
                    #     self.goals = [(1, 1)]
                    #     sim.setAgentPosition(self.agent, (0, 0))
                else:
                    x = len(self.velocity)
                    #for i in range(0):
                    y = [self.velocity[x-2][0], self.velocity[x-2][1]]
                    sim.setAgentPrefVelocity(self.agent,tuple(y))
                    if sim.queryVisibility(self.get_position(), tuple(self.goals[self.current_goal+1]), radius=0.3):
                        self.set_velocity(self.goals[self.current_goal])

            else:
                self.set_velocity(self.goals[self.current_goal])


class Agents:

    def __init__(self):
        self.agents = []
        self.trajectory = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def get_chart(self):
        for i in obstacles:
            sim.addObstacle(i)
        sim.processObstacles()

        for step in range(2500):
            trajector = []
            for agent in self.agents:
                agent.step()
                trajector.append(agent.get_position())
            self.trajectory.append(trajector)
            sim.doStep()

    def get_trajectory(self):
        return self.trajectory

egman = open("egman.json", 'r')
data = json.load(egman)["1"]["EVACUEES"]
obst = open("geom.json", "r")
obstacles = json.load(obst)["obstacles"]["1"]
A = Agents()

for i in data:
    pretime = data[i]["PRE_EVACUATION"]
    position = tuple(data[i]["ORIGIN"])
    goals = data[i]["ROADMAP"]
    speed = data[i]["H_SPEED"]
    A.add_agent(Agent(goals, pretime, speed, position))

class Animation:

    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-1, 60), ylim=(-1, 20))
        self.trial = []
        self.create_walls()
        self.trajectory = A.get_trajectory()
        self.n_frames = len(self.trajectory)
        elipses = [mpaths.Ellipse(i, width=1, height=1, angle=0) for i in self.trajectory[0]]
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

    def create_walls(self):
        for i in obstacles:
            corners_x = [i[0][0], i[1][0], i[2][0], i[3][0]]
            corners_y = [i[0][1], i[1][1], i[2][1], i[3][1]]
            plt.plot(corners_x, corners_y, "k", lw=2)

A.get_chart()
B = Animation()
B.create_walls()
B.do_animation(30)

