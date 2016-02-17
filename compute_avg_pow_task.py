import csv
import sys
import numpy as np
import scipy as sp
import scipy.stats

with open(sys.argv[1], 'r') as inp:
    reader = csv.reader(inp)
    tot_pw = 0.0
    first = True
    pw = []
    # calculate tot_pw
    for row in reader:
        if first:
            first_time = float(row[0])  # first timestamp
            first = False
        pw.append(float(row[2]))
    last_time = float(row[0]) # last timestamp
    tot_time = last_time - first_time
    avg = np.average(pw)/1000
    stand = np.std(pw)/1000 # print W consumed and standard deviation
    # extract file name (value of times task executed)
    extr = sys.argv[1].split("-")
    key = int(extr[1])
    print (key)
    print (avg, stand)
    inp.close()
