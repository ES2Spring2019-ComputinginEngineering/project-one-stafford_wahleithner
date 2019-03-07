import numpy as np
import matplotlib.pyplot as plt

length = [0.2, 0.255, 0.38, 0.495, 0.72]
real_period = [0.8047, 0.975, 1.1476, 1.3198, 1.5627]
simulation_period = [0.9584, 1.0749, 1.293, 1.4808, 1.781]

log_length = np.log10(length)
log_real_period = np.log10(real_period)
log_simulation_period = np.log10(simulation_period)

plt.figure(figsize = (6,4))

plt.subplot(2,1,1)
plt.plot(log_length, log_real_period, 'r-') 
plt.xlabel('Length (m)')
plt.ylabel('Period (seconds)')
plt.title('Real Data Period vs Length')
plt.xlim((-0.8, 0))
plt.grid()
plt.tight_layout()
plt.show()

plt.subplot(2,1,2)
plt.plot(log_length, log_simulation_period, 'r-') 
plt.xlabel('Length (m)')
plt.ylabel('Period (seconds)')
plt.title('Simulation Period vs Length')
plt.xlim((-0.8, 0))
plt.grid()
plt.tight_layout()
plt.show()

slope, intercept = np.polyfit(log_length, log_simulation_period, 1)
print("Simulation: \n Slope: ", slope, "\n Intercept: ", intercept)
slope, intercept = np.polyfit(log_length, log_real_period, 1)
print("Real Data: \n Slope: ", slope, "\n Intercept: ", intercept)

