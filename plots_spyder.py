#check: confirm equations, how to add plots to file (+ need file?), 
#how to get velocity/acceleration graphs, format plots (period), report, due date time!!
#actually measure pendulum

import matplotlib.pyplot as plt
import math as m
import numpy as np
import scipy.signal as sig
import os
cwd = os.getcwd()
os.chdir("C:\\Users\zosia\mu_code")

filename = input("What is the filename? ")
fin = open(filename) #Get microbit data file name


a = []
ang_list = []
vel_list = []
acc_list = []
t_list = []

#Parsing the microbit file
for line in fin:
    word = line.strip()
    delimeter = ","
    a = word.split(delimeter)
    #Find each value from commas:
    t = float(a[0])
    x = float(a[1])
    y = float(a[2])
    z = float(a[3])
    
    #Get list of time
    t_list.append(t)
    #Get list of angles
    ang = m.atan2(y,(m.sqrt(x**2+z**2)))
    ang_list.append(ang)
    
    #Get list of velocity by differentiating
for i in range(len(ang_list)-1):
    ang_diff = ang_list[i+1] - ang_list[i]
    time_diff = t_list[i+1] - t_list[i]
    vel = ang_diff / time_diff
    vel_list.append(vel)
    
    #Get list of acceleration by differentiating
for i in range(len(vel_list)-1):
    vel_diff = vel_list[i+1] - vel_list[i]
    time_diff = t_list[i+1] - t_list[i]
    acc = vel_diff / time_diff
    acc_list.append(acc)
    

#Plot data
plt.figure(figsize = (4,6))

plt.subplot(3,1,1)
plt.plot(t_list, ang_list, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (rad)')
plt.title('Angle vs Time')
plt.xlim((0, float(a[0])))
plt.grid()
plt.tight_layout()
plt.show()
fin.close()

#We only need the angle graph, but these are the functions to get velocity and acceleration:

#plt.subplot(3,1,2)
#plt.plot(t_list[:-1], vel_list, 'b-') 
#plt.xlabel('Time (seconds)')
#plt.ylabel('Angular Velocity (rad/s)')
#plt.title('Angular Velocity vs Time')
#plt.xlim((0, float(a[0])))
#plt.grid()

#plt.subplot(3,1,3)
#plt.plot(t_list[:-2], acc_list, 'k-') 
#plt.xlabel('Time (seconds)')
#plt.ylabel('Angular Acceleration (rad/s^2)')
#plt.title('Angular Acceleration vs Time')
#plt.xlim((0, float(a[0])))
#plt.grid()

#Cutting our graph to when the pendulum was moving in harmonic motion
time = np.array(t_list[20:285])
y = np.array(ang_list[20:285])

# Apply median filter to both original and noisy wave
y_filt = sig.medfilt(y, 7)

# Find peaks of all waves
y_pks, _ = sig.find_peaks(y)

y_filt_pks, _ = sig.find_peaks(y_filt)

# Plot waveforms and their peaks
plt.subplot(2,1,1)
plt.plot(time, y, 'r-', time[y_pks], y[y_pks], 'b.')
plt.title('Original')

plt.subplot(2,1,2)
plt.plot(time, y_filt, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
plt.title('Original Median Filtered')

plt.tight_layout()
plt.show()

#Find period
intersect_list = []     #when the graph intersects the x axis
period_list = []        #the time distance between every other x intersection

for i in range(len(y_filt)):
    #when it goes from positive to negative (these are half of the intersects)
    if y_filt[i] < 0 and y_filt[i+1] > 0:
        p = (t_list[i+1] + t_list[i]) / 2
        intersect_list.append(p)
for i in range(len(intersect_list)-2):
    m = intersect_list[i+1] - intersect_list[i]
    period_list.append(m)
period_average = sum(period_list) / len(period_list)
print("Average period:  ", period_average)

#Find peaks
#peaks_angle = []
#peaks_time = []
#for i in range(len(ang_list[20:285])-2):
#    if ang_list[i] > ang_list[i-1] and ang_list[i] > ang_list[i+1]:
#        peaks_angle.append(ang_list[i])
#        peaks_time.append(t_list[i])
#print("peaks_angle:  ", peaks_angle)
#print("peaks_time:  ", peaks_time)
