#check: confirm equations, how to add plots to file (+ need file?), 
#how to get velocity/acceleration graphs, format plots (period), report, due date time!!
#actually measure pendulum

import matplotlib.pyplot as plt
import math as m
import os
cwd = os.getcwd()
os.chdir("C:\\Users\zosia\mu_code")

filename = input("What is the filename? ")
fin = open(filename)


a = []
ang_list = []
vel_list = []
acc_list = []
t_list = []

for line in fin:
    word = line.strip()
    
    delimeter = ","
    a = word.split(delimeter)
    
    t = float(a[0])
    x = float(a[1])
    y = float(a[2])
    z = float(a[3])
    
    ang = m.atan2(x,(m.sqrt(y**2+z**2)))
    ang_list.append(ang)
    t_list.append(t)
    
for i in range(len(ang_list)-1):
    ang_diff = ang_list[i+1] - ang_list[i]
    time_diff = t_list[i+1] - t_list[i]
    vel = ang_diff / time_diff
    vel_list.append(vel)

for i in range(len(vel_list)-1):
    vel_diff = vel_list[i+1] - vel_list[i]
    time_diff = t_list[i+1] - t_list[i]
    acc = vel_diff / time_diff
    acc_list.append(acc)
    


#Plots
plt.figure(figsize = (4,6))

plt.subplot(3,1,1)
plt.plot(t_list, ang_list, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (rad)')
plt.title('Angle vs Time')
plt.xlim((0, float(a[0])))
plt.grid()

plt.subplot(3,1,2)
plt.plot(t_list[:-1], vel_list, 'b-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Angular Velocity vs Time')
plt.xlim((0, float(a[0])))
plt.grid()

plt.subplot(3,1,3)
plt.plot(t_list[:-2], acc_list, 'k-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rad/s^2)')
plt.title('Angular Acceleration vs Time')
plt.xlim((0, float(a[0])))
plt.grid()
plt.tight_layout()
plt.show()

fin.close()



#period_list = []
#for i in ang_list:
 #   if ang_list[i] < 0 and ang_list[i+1] > 0:
  #      p = t_list[i+1] - t_list[i]
   #     period_list.append(p)
        
        