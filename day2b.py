#!/bin/python
# Advent of Code 2017 - Day 2b

import csv
spreadsheet = csv.reader(open('day2input.txt', 'rb'), delimiter='\t')
checksum = 0
for row in spreadsheet:
    row = map(int, row)
    for a in range(len(row)):
        for b in range(len(row)):
            if a == b: continue
            if row[a] % row[b] == 0:
                checksum += row[a] / row[b]
print "Final checksum: " + str(checksum)
