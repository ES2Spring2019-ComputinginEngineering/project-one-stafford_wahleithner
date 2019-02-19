import from microbit *
import numpy as np

def update_system(acc,pos,vel,time1,time2):
    dt = time2 - time2
    pos_Next =
    vel_Next =
    return pos_Next, vel_Next

def print_system(time,pos,vel):
    print("TIME:    ", time)
    print("POSITION:    ", pos)
    print("VELOCITY:    ", vel, '\n')

#initial conditions
pos = [0]
vel = [0]
acc = [0,1,2,3,4,4,2,2,1,0,0,0,0,-1,-1,-2,-2,-2,-3,-4,-4]

i = 1
while i < len(time):
    #update position and velocity using previous values and time step
    pos_Next, vel_Next = update_system(acc[i], pos[i - 1], vel[i -1], time[i - 1], time[i])
    pos.append(pos_Next)
    vel.append(vel_Next)
    print_system(time[i], pos[i], vel[i])
    i =+ 1
time = np.linspace(0,20,21)
print_system(time[0],pos[0], vel[0])