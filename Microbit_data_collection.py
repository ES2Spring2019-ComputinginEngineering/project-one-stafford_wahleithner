#Names: Zosia Stafford and Gillian Wahleithner
#Microbit_data_collection.py:
    #Creates and writes to a new file on microbit
    #When button A is pressed, it begins collecting data
    #Collects accelerometer values and the current time
    #Writes time, acc x, acc y, acc z separated by commas
    #Writes each new data point in a new line

from microbit import *
import math
import random as r

filename = "data_" + str(r.randint(1,999)) + ".txt"
with open(filename, "w") as data:
    while not button_a.is_pressed():
        sleep(50)
    start_time = running_time()
    while not button_b.is_pressed():
        ax = accelerometer.get_x()
        ay = accelerometer.get_y()
        az = accelerometer.get_z()
        elapsed_time = (running_time() - start_time) / 1000
        numbers = str(elapsed_time) + ", " + str(ax) + ", " + str(ay) + ", " + str(az) + "\r\n"
        data.write(numbers)
        sleep(20)
    data.close()