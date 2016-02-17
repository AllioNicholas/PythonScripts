import csv
import sys

name_input = sys.argv[2].split(".")[0] # extract input file name
down_file = name_input + "-down.csv"

with open(sys.argv[2], 'r') as inp, open(down_file, 'w') as outp:
    writer = csv.writer(outp)
    reader = csv.reader(inp)
    count = 0
    for row in reader:
        if count % int(sys.argv[1]) == 0:
            writer.writerow(row)
        count +=1
    outp.close()
    inp.close()
