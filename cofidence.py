import numpy as np
import scipy as sp
import scipy.stats
import csv
from collections import defaultdict
import statistics

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t.ppf((1+confidence)/2., n-1)
    return h

with open('loc_res.csv', 'r') as csvfile, open('conf-95.csv', 'a') as writfile:
    writer = csv.writer(writfile)
    reader = csv.reader(csvfile)
    writer.writerow(["Key","AVG"])
    els = defaultdict(list)
    for row in reader:
        els[row[0]].append(float(row[1]))

    for key in els:
        writer.writerow([key, statistics.mean(els[key]), mean_confidence_interval(els[key])])
    writfile.close()
