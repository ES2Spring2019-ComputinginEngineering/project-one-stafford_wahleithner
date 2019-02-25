import numpy as np
import math as m

g = -9.81

def update_system(acc,ang,vel,time1,time2):
    dt = time2 - time1
    ang_Next = ang + (vel * dt)
    vel_Next = vel + (acc * dt)
    acc_Next = (g)*(m.sin(ang_Next))
    return ang_Next, vel_Next, acc_Next

def print_system(time,ang,vel,acc):
    #print("TIME:    ", time)
    #print("ANGLE:    ", ang)
    #print("ANGULAR VELOCITY:    ", vel)
    #print("ACCELERATION:    ", acc, '\n')
    print((ang, vel, acc))

#initial conditions
ang = [m.pi/4]
vel = [0]
acc = [(g)*(m.sin(ang[0]))]

time = np.linspace(0,20,20001)
print_system(time[0],ang[0], vel[0], acc[0])


i = 1
while i < len(time):
    #update angle and velocity using previous values and time step
    ang_Next, vel_Next, acc_Next = update_system(acc[i-1], ang[i - 1], vel[i -1], time[i - 1], time[i])
    ang.append(ang_Next)
    vel.append(vel_Next)
    acc.append(acc_Next)
    print_system(time[i], ang[i], vel[i], acc[i])
    i += 1