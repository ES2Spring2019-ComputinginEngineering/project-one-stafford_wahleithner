import matplotlib.pyplot as plt
import numpy as np

def open_file(filename):
    fin = open(filename)
    new = open("data_plots.py", 'w+')
    
    t = []
    
    for line in fin:
        count = 0
        i = 0
        word = line.strip()
        
        delimeter = ","
        t = word.split(delimeter)
