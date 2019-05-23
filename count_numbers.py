#!/usr/bin/python

# Read in CSV file of iter counts and count each number.
# Row 1 contains Size info for printing CSV file as PNG.
# JM Thu  8 Mar 2018 20:50:30 GMT

import csv
import sys

iter_list = []
iter_dict = {}

fname = sys.argv[ 1 ]

with open( fname ) as f:
	reader = csv.reader(f)
	row1 = next(reader)

        print 'Row1:', row1
	for row in reader:
		#print 'Row:', row
		iter_count = int( row[ 2 ] )

		if ( iter_count not in iter_list ):
			iter_list.append( iter_count )

		if ( iter_count not in iter_dict ):
			iter_dict[ iter_count ] = 1
		else:	
			iter_dict[ iter_count ] += 1
iter_list.sort()

print 'Iter:', iter_list
#print 'IterD:', iter_dict
print

for key in sorted( iter_dict ):
	print key, ' : ', iter_dict[ key ]
'''
'''


