import csv
import sys
import numpy as np
import scipy as sp
import scipy.stats
# TODO: change name of output file according to what you input

# write titles first
with open('bar_entries_combo.csv', 'w') as outp:
    writer = csv.writer(outp)
    writer.writerow(["Instructions", "AVG Power"])
    outp.close()

# write data afterward
args = sys.argv
args.pop(0)
for fil in args:
    with open(fil, 'r') as inp, open('bar_entries_combo.csv', 'a') as outp:
        writer = csv.writer(outp)
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
        # extract file name (value of parameter tested)
        extr = fil.split(".")
        key = int(extr[0])
        # wite row in csv output file
        writer.writerow([key, np.average(pw)/1000, np.std(pw)/1000]) # save key, W consumed and standard deviation
        # writer.writerow([first_time, last_time])
        outp.close()
        inp.close()
