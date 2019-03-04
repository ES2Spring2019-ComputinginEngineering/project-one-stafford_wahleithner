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
new = open("data_plots.py", 'w+')

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
    vel = ang/t
    acc = -9.81/(15*m.sin(ang))
    
    ang_list.append(ang)
    vel_list.append(vel)
    acc_list.append(acc)
    t_list.append(t)

print(ang_list)
print("****")
print(vel_list)
print("****")
print(acc_list)
print("****")
print(t_list)

plot = plt.figure(figsize = (4,6))

plt.subplot(3,1,1)
plt.plot(t_list, ang_list, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (rad)')
plt.title('Angle vs Time')
plt.xlim((0, a[0]))
plt.grid()


plt.subplot(3,1,2)
plt.plot(t_list, vel_list, 'b-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Angular Velocity vs Time')
plt.xlim((0, a[0]))
plt.grid()


plt.subplot(3,1,3)
plt.plot(t_list, acc_list, 'k-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rad/s^2)')
plt.title('Angular Acceleration vs Time')
plt.xlim((0, a[0]))
plt.grid()
plt.tight_layout()
plt.show()

new.write(plot)
fin.close()
new.close()

