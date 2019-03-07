#Names: Gillian Wahleithner and Zosia Stafford
#Real_data_parsing.py:
    #Parses data from txt file (gets angles and times)
    #graphs angle vs time
    #graphs significant data (when in harmonic motion)
    #graphs filtered data with peaks marked
    #returns angles and times of peaks and period

#This will run on our Test_data.txt, which is data from length 3

import matplotlib.pyplot as plt
import math as m
import numpy as np
import scipy.signal as sig

filename = input("What is the filename? ")
fin = open(filename) #Get microbit data file name

#start and end of significant data, used in line 64
s = 20
e = 285

a = []
ang_list = []
vel_list = []
acc_list = []
t_list = []
x_list = []
y_list = []

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

#Plot angle vs time
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

#Cutting our graph to when the pendulum moves in harmonic motion
time = np.array(t_list[s:e])
y = np.array(ang_list[s:e])

# Apply median filter to our angle and time array
y_filt = sig.medfilt(y, 7)
time_filt = sig.medfilt(time, 7)
# Find peaks of waves
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