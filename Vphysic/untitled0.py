
import vpython as vp

monitor = vp.canvas(title = "uniform accelerated motion")
ground = vp.box(pos = vp.vector(0, 0, 0), size = vp.vector(5, 0.4, 2), center = vp.vector(0, 0.3, 0))
cube = vp.box(pos = vp.vector(-2.4, 0.3, -0.8), size = vp.vector(0.2, 0.2, 0.2), color = vp.color.purple)

a = 0.03
v = 0
dt = 0.01

#print(cube.pos.x)
while cube.pos.x < 2.4:
    vp.rate(1000)
    cube.pos.x += dt * v
    v += a * dt
    print(cube.pos.x)
