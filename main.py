import numpy as np
import uav_trajectory
#绘制静态图include
# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
#绘制动态图include
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import animation


traj = uav_trajectory.Trajectory()
traj.loadcsv("figure8.csv")
offset = np.array([0,0,0.5])
tarray = np.arange(0.1, 7, 0.1)
print(tarray)
x=[]
y=[]
z=[]
for t in tarray:
    e = traj.eval(t)
    pos = e.pos+offset
    vel = e.vel
    acc = e.acc
    yaw = e.yaw
    omega = e.omega
    print("duration:",traj.duration)
    print("pos:",pos)
    print("vel:",vel)
    print("acc:",acc)
    print("yaw:",yaw)
    print("omega:",omega)
    x.append(pos[0])
    y.append(pos[1])
    z.append(pos[2])

#绘制静态图
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()

#绘制动态图
fig, ax = plt.subplots()

l = ax.plot(x, y)

dot1, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(-55, 55)
    ax.set_ylim(-55, 55)
    return l

#generate
def gen_dot1():
    for index,val in enumerate(x):
        newdot = [val, y[index]]
        yield newdot


#update
def update_dot1(newd):
    dot1.set_data(newd[0], newd[1])
    return dot1,

# ani = animation.FuncAnimation(fig, update_dot, frames=gen_dot, interval=100, init_func=init)
ani1 = animation.FuncAnimation(fig, update_dot1, frames=gen_dot1, interval=100)
ani1.save('sin_dot.gif', writer='imagemagick', fps=30)

plt.show()
