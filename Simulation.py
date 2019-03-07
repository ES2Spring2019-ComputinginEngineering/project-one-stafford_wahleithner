import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy.signal as sig

g = -9.81
l= 0.38

def update_system(acc,ang,vel,time1,time2):
    dt = time2 - time1
    ang_Next = ang + (vel * dt)
    vel_Next = vel + (acc * dt)
    acc_Next = g/l*m.sin(ang)
    return ang_Next, vel_Next, acc_Next

#initial conditions
ang = [m.pi/4]
vel = [0]
acc = [0]
time = np.linspace(0,10,10001)

#update angle and velocity using previous values and time step
i = 1
while i < len(time):
    ang_Next, vel_Next, acc_Next = update_system(acc[i-1], ang[i - 1], vel[i -1], time[i - 1], time[i])
    ang.append(ang_Next)
    vel.append(vel_Next)
    acc.append(acc_Next)
    i += 1

plt.figure(figsize = (4,6))
plt.subplot(3,1,1)
plt.plot(time, ang, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (rad)')
plt.title('Angle vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()

plt.subplot(3,1,2)
plt.plot(time, vel, 'b-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Angular Velocity vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()

plt.subplot(3,1,3)
plt.plot(time, acc, 'k-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rad/s^2)')
plt.title('Angular Acceleration vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()
plt.show()

#Find Peaks
time_a = np.array(time)
ang_a = np.array(ang)
ang_peaks, _ = sig.find_peaks(ang_a)

peaks = ang_peaks
ang_peaks_list = np.ndarray.tolist(ang_a[peaks])
time_peaks_list = np.ndarray.tolist(time_a[peaks])
print("Peaks of Angle vs. Time graph:")
print("Angle of Peaks: ", ang_peaks_list)
print("Time of Peaks: ", time_peaks_list)

#Find Period
period_list = []
for i in range(len(time_peaks_list)-1):
    m = time_peaks_list[i+1] - time_peaks_list[i]
    period_list.append(m)
period_average = sum(period_list) / len(period_list)
print("Average Period:  ", period_average, " seconds")
