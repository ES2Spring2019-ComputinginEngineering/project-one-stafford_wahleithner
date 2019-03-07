#Names: Zosia Stafford and Gillian Wahleithner
#Period_Analysis.py:
    #Takes a list of lengths, simulation periods, and real world periods
    #plots the length vs period for both simulation and real world data
    #takes the log of lists and turns them into arrays
    #plots the log length vs log period for both simulation and real world data to get a linear graph
    #find the slope and y intercept of these linear graphs

import numpy as np
import matplotlib.pyplot as plt

#Data from Real_data_parsing.py
length = [0.2, 0.255, 0.38, 0.495, 0.72]
real_period = [0.8047, 0.975, 1.1476, 1.3198, 1.5627]
simulation_period = [0.9584, 1.0749, 1.293, 1.4808, 1.781]

#Make into log graphs
log_length = np.log10(length)
log_real_period = np.log10(real_period)
log_simulation_period = np.log10(simulation_period)

#Plot orginal data
plt.figure(figsize = (5,3))
plt.plot(length, real_period, 'r-') 
plt.xlabel('Length (m)')
plt.ylabel('Period (seconds)')
plt.title('Real Data Period vs Length')
plt.xlim((0, 1))
plt.grid()
plt.tight_layout()
plt.show()

plt.figure(figsize = (5,3))
plt.plot(length, simulation_period, 'r-') 
plt.xlabel('Length (m)')
plt.ylabel('Period (seconds)')
plt.title('Simulation Period vs Length')
plt.xlim((0, 1))
plt.grid()
plt.tight_layout()
plt.show()

#Plot logarithmic data
plt.figure(figsize = (5,3))
plt.plot(log_length, log_real_period, 'r-') 
plt.xlabel('Log of Length (m)')
plt.ylabel('Log of Period (seconds)')
plt.title('Real Data Log Period vs Log Length')
plt.xlim((-0.8, 0))
plt.grid()
plt.tight_layout()
plt.show()

plt.figure(figsize = (5,3))
plt.plot(log_length, log_simulation_period, 'r-') 
plt.xlabel('Log of Length (m)')
plt.ylabel('Log of Period (seconds)')
plt.title('Simulation Log Period vs Log Length')
plt.xlim((-0.8, 0))
plt.grid()
plt.tight_layout()
plt.show()

#Find the slope and intercept of linear graphs
slope, intercept = np.polyfit(log_length, log_simulation_period, 1)
print("Simulation: \n Slope: ", slope, "\n Intercept: ", intercept)
slope, intercept = np.polyfit(log_length, log_real_period, 1)
print("Real Data: \n Slope: ", slope, "\n Intercept: ", intercept)

