#!/bin/python
# Advent of Code 2017 - Day 4a

import csv
import collections

spreadsheet = csv.reader(open('day4input.txt', 'rb'), delimiter=' ')
i = 0
total = 0
for row in spreadsheet:
    state = True
    counter = collections.Counter(row)
    for i in counter:
        if counter[i] > 1:
            state = False
    if state == True:
        total += 1
print "Passphrases: " + str(total)
