from vpython import *
scene.forward = vector(0.6, -0.5, -1)

box(size=vector(10, 0.5, 21.5), color=color.green)
box(size=vector(10, 0.01, 21.5), pos=vector(0,-0.25,0), texture=textures.wood)
box(size=vector(8,4,20),pos=vector(0,-2.2,0), texture=textures.wood)
box(size=vector(11,1.5,0.5),pos=vector(0,0.5,11),texture=textures.wood)
box(size=vector(10,1.5,0.01),pos=vector(0,0.5,10.75),color=color.green)
box(size=vector(11,1.5,0.5),pos=vector(0,0.5,-11),texture=textures.wood)
box(size=vector(10,1.5,0.01),pos=vector(0,0.5,-10.75),color=color.green)
box(size=vector(0.5,1.5,21.5),pos=vector(5.25,0.5,0),texture=textures.wood)
box(size=vector(0.01,1.5,21.5),pos=vector(5,0.5,0),color=color.green)
box(size=vector(0.5,1.5,21.5),pos=vector(-5.25,0.5,0),texture=textures.wood)
box(size=vector(0.01,1.5,21.5),pos=vector(-5,0.5,0),color=color.green)

MAXPOZX = 4.5
MAXPOZZ = 10.25
BILE = []

BILE.append(sphere(pos=vector(1,0.65,2), radius=0.5, color=color.red))
BILE.append(sphere(pos=vector(-1,0.65,-2), radius=0.5, color=color.red))

BILE.extend([sphere(pos=vector(4.4,0.65,0), radius=0.5, color=color.red), sphere(pos=vector(-4.4,0.65,0), radius=0.5, color=color.red), sphere (pos=vector(0,0.65,0), radius=0.5, color=color.black), sphere (pos=vector(0,0.65,10.25), radius=0.5, color=color.blue), sphere (pos=vector(0,0.65,-10.25), radius=0.5, color=color.blue), sphere (pos=vector(0,0.65,5), radius=0.5, color=color.white)])

for i in range(len(BILE)):
    BILE[i].velocity = vector(1,0,1)

dt = 0.15
def zderzenie_bandy(balls):
    for ball in balls:
        if ball.pos.x >= MAXPOZX or ball.pos.x <= -MAXPOZX:
            ball.velocity.x = -ball.velocity.x
        elif ball.pos.z >= MAXPOZZ or ball.pos.z <= -MAXPOZZ:
            ball.velocity.z = -ball.velocity.z

def zderzenie_innej(balls):
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            dystans = mag2(balls[i].pos - balls[j].pos)
            if dystans < (2*0.65)**2:
                v = norm(balls[j].pos - balls[i].pos)
                balls[i].velocity = -v
                balls[j].velocity = v
def ruch(balls):
    for ball in balls:
        ball.pos += ball.velocity*dt


while True:
    rate(50)
    zderzenie_innej(BILE)
    zderzenie_bandy(BILE)
    ruch(BILE)
