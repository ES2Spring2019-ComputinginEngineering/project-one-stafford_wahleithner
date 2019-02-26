from microbit import *
import math

import os
cwd = os.getcwd()
os.chdir("C:\\Users\zosia\onedrive\documents\college\intro to computing")

with open("pendulum_data.txt", "w+")
start_time = running_time()
while not button_b.is_pressed():
    sleep(50)
while not button_a.is_pressed():
    ax = accelerometer.get_x()
    ay = accelerometer.get_y()
    az = accelerometer.get_z()
    elapsed_time = running_time() - start_time
    write = (str(elapsed_time) + ", " + str(ax) + ", " + str(ay) + ", " str(az) + "/n")
    file.write(write)
    sleep(50)