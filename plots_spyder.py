import matplotlib.pyplot as plt
import numpy as np
import math as m
    

def open_file(filename):
    fin = open(filename)
    new = open("data_plots.py", 'w+')
    
    a = []
    
    for line in fin:
        count = 0
        i = 0
        word = line.strip()
        
        delimeter = ","
        a = word.split(delimeter)
        
        t = a[0]
        x = a[1]
        y = a[2]
        z = a[3]
        ang = m.atan2(x,(math.sqrt(y**2+z**2)))
        vel =
        acc =

