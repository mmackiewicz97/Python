import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
from matplotlib.patches import Arrow
A1x=1
A1y=1
B1x=20
B1y=4
v1 = 3
dx1 = (B1x-A1x)/((B1x-A1x)**2+(B1y-A1y)**2)**(1/2)
dy1 = (B1y-A1y)/((B1x-A1x)**2+(B1y-A1y)**2)**(1/2)
C1x = 50
C1y = 2
v11 = 1
dx11 = (C1x-B1x)/((C1x-B1x)**2+(C1y-B1y)**2)**(1/2)
dy11 = (C1y-B1y)/((C1x-B1x)**2+(C1y-B1y)**2)**(1/2)
step = 30

class Anim:

    def __init__(self):
        self.fig = plt.figure()
        self.pedestrians= []
        self.ax = plt.axes(xlim=(0,70),ylim=(0,6))
        self.n_frames = 0
        self.trajectory = []
        self.elipsy = []
        self.strzal = []
        self.x = 0
        self.y = 0
        self.z = [(A1x,A1y)]
        self.trajectory.append(self.z)
        z=step
        plt.plot(A1x, A1y, "v")
        plt.text(A1x, A1y, "A")
        plt.plot(B1x, B1y, "v")
        plt.text(B1x, B1y, "B")
        plt.plot(C1x, C1y, "v")
        plt.text(C1x, C1y, "C")
        for i in range(0, step) :
            x = [(A1x+(i*dx1*v1),A1y+(i*dy1*v1))]
            z-=1
            if self.trajectory[i][0][0] < B1x:
                self.trajectory.append(x)
            else:
                break
        print("Zatrzymano w punkcie: ",self.trajectory[i][0][0]," : ",self.trajectory[i][0][1])
        print("Punkt B: ", B1x,":" ,B1y)
        self.x = i
        for j in range(z):
            x = [(A1x + ((i-1) * dx1 * v1)+(j * dx11 * v11), A1y + ((i-1) * dy1 * v1)+(j * dy11 * v11))]
            self.trajectory.append(x)
        self.n_frames = len(self.trajectory)
        ellipses = [Ellipse(i, width=2 ,height=0.2 ,angle=0) for i in self.trajectory[0]]
        [self.elipsy.append(self.ax.add_patch(ellipses[i])) for i in range(len(ellipses))]

    def init_animation(self):
        [self.elipsy[i].set_visible(True) for i in range(len(self.elipsy))]
        [self.strzal[i].set_visible(True) for i in range(len(self.strzal))]
        return self.elipsy + self.strzal

    def animate (self, i):
        self.strzal = []
        for j in range(len(self.elipsy)):
            self.y+=1
            if self.y <= self.x:
                self.elipsy[j].center = self.trajectory[i][j]
                strzalka = Arrow(self.trajectory[i][0][0], self.trajectory[i][0][1], dx1, dy1, width=1, color="r")
                self.strzal.append(self.ax.add_patch(strzalka))
            else:
                self.elipsy[j].center = self.trajectory[i][j]
                strzalka = Arrow(self.trajectory[i][0][0], self.trajectory[i][0][1], dx11, dy11, width=1, color="g")
                self.strzal.append(self.ax.add_patch(strzalka))
        return self.elipsy + self.strzal

    def do_animation(self, n_interval):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_animation, frames=self.n_frames, interval=n_interval, blit=True)
        plt.show()

Anim().do_animation(300)
