#!/bin/python
# Advent of Code 2017 - Day 2a

import csv
spreadsheet = csv.reader(open('day2input.txt', 'rb'), delimiter='\t')
for row in spreadsheet:
	print(row)