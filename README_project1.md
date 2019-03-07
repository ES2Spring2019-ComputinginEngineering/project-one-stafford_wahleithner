# Project 1: Micro:bit Pendulum

Create a simulation of a pendulum, then collect data from a physical pendulum and compare graphs and periods.

## Overview

The file Simulation.py will run a simulation of a pendulum with a starting angle of pi/4. 
It will output graphs of angle, angular velocity, and angular acceleration. It will also give 
a list of peak angles and times, and the period of the angle vs time graph.

The file Microbit_data_collection.py is the mu file we flash to our microbit to collect data
from a physical pendulum. Once flashed, the A button will start it, and the B button will stop it.

The Real_data_parsing.py is our code that parses this file and returns a graph of angle vs time, 
a graph of significant data (after the pendulum starts moving and before we stop it), and a filtered
graph with the peaks marked. It also returns a list of peak angles and times, as well as period. 
This file is designed to read our data from length 3, titled Test_data.txt. For other data files, 
we would change our bounds s and e (in line for 15) where the significant data is. We have a section of
code commented out, which if uncommented will return a graph of acceleration.

Real_data_parsing.py will ask for the file name, which in this case is Test_data.txt.
    
We also have a file Period_analysis.py, which has a list of our lengths and periods and returns
graphs of the relationship between period and length of a pendulum.

## Structure of our codes:

Simulation.py:
- set initial conditions
- update system according to our equations
- for a specified time, update values into lists
- graph lists of angles, angular velocity, and angular acceleration
- find peaks, return peak angles and time and calculate period

Microbit_data_collection.py:
- Creates and writes to a new file on microbit
- When button A is pressed, it begins collecting data
- Collects accelerometer values and the current time
- Writes time, acc x, acc y, acc z separated by commas
- Writes each new data point in a new line

Test_data.txt:
- time, x acceleration, y acceleration, z acceleration
- separated by commas, each new line is a new data point
    
Real_data_parsing.py:
- Parses data from txt file (gets angles and times)
- graphs angle vs time
- graphs significant data (when in harmonic motion)
- graphs filtered data with peaks marked
- returns angles and times of peaks and period

Period_Analysis.py:
- Takes a list of lengths, simulation periods, and real world periods
- plots the length vs period for both simulation and real world data
- takes the log of lists and turns them into arrays
- plots the log length vs log period for both simulation and real world data to get a linear graph
- find the slope and y intercept of these linear graphs

Thanks! :)
