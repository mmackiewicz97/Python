import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
from matplotlib.patches import Arrow
A1x=1
A1y=1
B1x=100
B1y=4
v1 = 3
A2x=3
A2y=4
B2x=70
B2y=3
v2 = 6
step = 30
dx2 = (B2x-A2x)/((B2x-A2x)**2+(B2y-A2y)**2)**(1/2)
dy2 = (B2y-A2y)/((B2x-A2x)**2+(B2y-A2y)**2)**(1/2)
dx1 = (B1x-A1x)/((B1x-A1x)**2+(B1y-A1y)**2)**(1/2)
dy1 = (B1y-A1y)/((B1x-A1x)**2+(B1y-A1y)**2)**(1/2)

class Anim:

    def __init__(self):
        self.fig = plt.figure()
        self.pedestrians= []
        self.ax = plt.axes(xlim=(0,200),ylim=(0,6))
        self.n_frames = 0
        self.trajectory = []
        f = range(1,step)
        self.strzalkia = []
        self.strzalkib = []
        self.elipsy = []
        self.strzal = []
        for i in f :
            x = [(A1x+(i*dx1*v1),A1y+(i*dy1*v1)),(A2x+(i*dx2*v2),A2y+(i*dy2*v2))]
            a = A1x+(i*dx1*v1)
            b = A1y+(i*dy1*v1)
            self.trajectory.append(x)
            self.strzalkia.append(a)
            self.strzalkib.append(b)
        self.n_frames = len(self.trajectory)
        ellipses = [Ellipse(i, width=2 ,height=0.2 ,angle=0) for i in self.trajectory[0]]
        strzalka = [Arrow(self.strzalkia[i], self.strzalkib[i], dx1, dy1, width=1, color="r") for i in range(len(self.strzalkia))]
        [self.elipsy.append(self.ax.add_patch(ellipses[i])) for i in range(len(ellipses))]
        [self.strzal.append(self.ax.add_patch(strzalka[i])) for i in range(len(ellipses))]
        print(self.trajectory[0][0][0])
        print("tekst")
    def init_animation(self):
        [self.elipsy[i].set_visible(True) for i in range(len(self.elipsy))]
        [self.strzal[i].set_visible(True) for i in range(len(self.strzal))]
        return self.elipsy + self.strzal

    def animate (self, i):
        self.strzal = []
        for j in range(len(self.elipsy)):
            self.elipsy[j].center = self.trajectory[i][j]
            strzalka = Arrow(self.strzalkia[i], self.strzalkib[i], dx1, dy1, width=1, color="r")
            strzalka2 = Arrow(self.trajectory[i][1][0], self.trajectory[i][1][1], dx2, dy2, width=1, color="g")
            self.strzal.append(self.ax.add_patch(strzalka))
            self.strzal.append(self.ax.add_patch(strzalka2))
            #strzal[j].x
        return self.elipsy + self.strzal

    def do_animation(self, n_interval):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_animation, frames=self.n_frames, interval=n_interval, blit=True)
        plt.show()

a = Anim()
a.do_animation(100)

#agent przechodzi przez 3 punkty
#zmiana wektora, prędkości