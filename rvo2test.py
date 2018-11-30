import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
import numpy as np
import rvo2

sim = rvo2.PyRVOSimulator(0.07, 1.5, 5, 1, 0.5, 0.55, 2)
#1/60. time step-ile sekund na dany krok [0.05/0.1]s
#neither distance - ile wcześniej zaczyna reagować by zmieniać kurs [1/1.5]m
#liczba agentów z którymi ma się minąć [5]
#time horizon-ograniczony stożek widoczności (zmienia już kurs) agent agent [1]s
#time horizon obstacle agent przeszkoda [0.5]s (jak najmniejszy aby agent podchodził blisko ściany) jeden krok czasowy
#local movement (nie ominie ściany, trzeba dodać global coś)
#radious(wielkość agenta,(koło))
#max speed długość wektora
#velocity-prędkość początkowa[tupla] wektor jednostkowy

#QueryVisibility- może się przełączyć na inny punkt gdy już go zobaczy

#gdzie agent, gdzie jego punkt, znormalizować i do biblioteki, norma-max speed

a0 = sim.addAgent((-5, 0))
a1 = sim.addAgent((2, 0))
a2 = sim.addAgent((0, 5))
a3 = sim.addAgent((0, -5))
a4 = sim.addAgent((-1, 3))

o1 = sim.addObstacle([(0.1, -8),(0.1,8)])
o2 = sim.addObstacle([(-0.5,2),(2,2)])
sim.processObstacles()

sim.setAgentPrefVelocity(a0, (1, 0))
sim.setAgentPrefVelocity(a1, (-1, 0))
sim.setAgentPrefVelocity(a2, (0, -1))
sim.setAgentPrefVelocity(a3, (0, 1))
sim.setAgentPrefVelocity(a4, (0.6, 0.2))
print('Simulation has %i agents and %i obstacle vertices in it.' % (sim.getNumAgents(), sim.getNumObstacleVertices()))

print('Running simulation')
trajectory = []
for step in range(700):
    sim.doStep()

    positions = ['(%5.3f, %5.3f)' % sim.getAgentPosition(agent_no) for agent_no in (a0, a1, a2, a3, a4)]
    print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))
    trajectory0 = [sim.getAgentPosition(agent_no) for agent_no in (a0, a1, a2, a3, a4)]
    trajectory.append(trajectory0)
class Animacja:
    def __init__(self):
        self.fig = plt.figure()
        self.pedestrians = []
        self.ax = plt.axes(xlim = (-6,6), ylim = (-6, 6))
        plt.plot([0.1, 0.1],[-8, 8])
        plt.plot([-0.5,2],[2,2])
        self.n_frames = 0
        self.trajectory = trajectory
        self.n_frames = len(self.trajectory)
        elip = [Ellipse(i, width=0.55, height=0.55, angle=0) for i in self.trajectory[0]]
        [self.pedestrians.append(self.ax.add_patch(elip[i])) for i in range(len(elip))]

    def init_animation(self):
        [self.pedestrians[i].set_visible(True) for i in range(len(self.pedestrians))]
        return self.pedestrians
    def animate(self, i):
        for j in range(len(self.pedestrians)):
            self.pedestrians[j].center = self.trajectory[i][j]
        return self.pedestrians
    def do_animation(self, n_interval):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_animation, frames=self.n_frames, interval=n_interval, blit=True)

        plt.show()

Animacja().do_animation(10)