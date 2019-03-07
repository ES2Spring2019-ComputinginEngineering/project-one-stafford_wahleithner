#This will run on our test_data, which is data from length 3

import matplotlib.pyplot as plt
import math as m
import numpy as np
import scipy.signal as sig
import os
cwd = os.getcwd()
os.chdir("C:\\Users\zosia\mu_code")

filename = input("What is the filename? ")
fin = open(filename) #Get microbit data file name

#start and end of significant data, used in line 72
s = 20
e = 285

a = []
ang_list = []
vel_list = []
acc_list = []
t_list = []
x_list = []
y_list = []
g = -9.81

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
    x_list.append(x)
    y_list.append(y)
    
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
plt.figure(figsize = (6,6))

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

#plt.subplot(3,1,3)
#plt.plot(t_list[s:e], y_list[s:e], 'k-') 
#plt.xlabel('Time (seconds)')
#plt.ylabel('Angular Acceleration (rad/s^2)')
#plt.title('Angular Acceleration vs Time')
#plt.xlim((0, float(a[0])))
#plt.grid()

#Cutting our graph to when the pendulum moves in harmonic motion
time = np.array(t_list[s:e])
y = np.array(ang_list[s:e])

# Apply median filter to both original and noisy wave
y_filt = sig.medfilt(y, 7)
time_filt = sig.medfilt(time, 7)
# Find peaks of all waves
y_pks, _ = sig.find_peaks(y, prominence = 0.05)
y_filt_pks, _ = sig.find_peaks(y_filt, prominence = 0.05)

# Plot waveforms and their peaks
plt.figure(figsize = (6,4))
plt.subplot(2,1,1)
plt.plot(time, y, 'r-', time[y_pks], y[y_pks], 'b.')
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (rad)')
plt.title('Original Angle vs Time, Significant Data')
plt.xlim((0, float(a[0])))
plt.grid()

plt.subplot(2,1,2)
plt.plot(time, y_filt, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (rad)')
plt.title('Median Filtered Angle vs Time')
plt.xlim((0, float(a[0])))
plt.grid()

plt.tight_layout()
plt.show()

#Find Peaks
peaks = y_filt_pks
y_peaks_list = np.ndarray.tolist(y[peaks])
time_peaks_list = np.ndarray.tolist(time[peaks])
print("Angle of Peaks: ", y_peaks_list)
print("Time of Peaks: ", time_peaks_list)

#Find Period
period_list = []
for i in range(len(time_peaks_list)-1):
    m = time_peaks_list[i+1] - time_peaks_list[i]
    period_list.append(m)
period_average = sum(period_list) / len(period_list)
print("Average Period:  ", period_average, " seconds")
    

