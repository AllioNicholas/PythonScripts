import csv
import sys

# write titles first
with open('bar_entries_byte.csv', 'w') as outp:
    writer = csv.writer(outp)
    writer.writerow(["Instructions", "AVG Power"])
    outp.close()

# write data afterward
args = sys.argv
args.pop(0)
for fil in args:
    with open(fil, 'r') as inp, open('bar_entries_byte.csv', 'a') as outp:
        writer = csv.writer(outp)
        reader = csv.reader(inp)
        tot_pw = 0.0
        num_samples = 0
        # calculate tot_pw
        for row in reader:
            tot_pw += float(row[2])
            num_samples += 1
        # extract file name (value of parameter tested)
        extr = fil.split(".")
        key = int(extr[0])
        # wite row in csv output file
        writer.writerow([key, tot_pw/num_samples])

        outp.close()
        inp.close()
