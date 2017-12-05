#!/bin/python
# Advent of Code 2017 - Day 2a

import csv
spreadsheet = csv.reader(open('day2input.txt', 'rb'), delimiter='\t')
i = 0
checksum = 0
for row in spreadsheet:
    row = map(int, row)
    highest = max(row)
    lowest = min(row)
    diff = int(highest) - int(lowest)
    checksum += diff
print "Final checksum: " + str(checksum)
