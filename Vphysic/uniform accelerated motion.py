
import vpython as vp

monitor = vp.canvas(title = "uniform accelerated motion", center = vp.vector(0, 0.3, 0))
ground = vp.box(pos = vp.vector(0, 0, 0), size = vp.vector(10, 0.4, 2))
cube = vp.box(pos = vp.vector(-4.9, 0.3, -0.8), size = vp.vector(0.2, 0.2, 0.2), color = vp.color.purple)

a = 0.1
v = 0
dt = 0.01

#print(cube.pos.x)
while cube.pos.x < 4.9:
    vp.rate(1000)
    cube.pos.x += dt * v
    v += a * dt
    print(cube.pos.x)
