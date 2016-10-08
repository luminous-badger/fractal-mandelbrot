#!/usr/bin/python

# Prints Mandelbrot set without need for numpy library.
# Points inside the set are represented by 'x', those outside by blanks.
# JM Sat  8 Oct 2016 15:14:36 BST

import cmath

x_min   = -20
x_max   =  10
y_min   = -10
y_max   =  10
offset  = 10.0
maxiter = 50

for Y in range ( y_min, y_max, 1 ):
	for X in range ( x_min, x_max, 1 ):

		Z = complex ( 0, 0 )
		C = complex ( X/offset, Y/offset )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = Z**2 + C
			iter_count = iter_count + 1
			#print X, Y 

		if ( iter_count < maxiter ):
			print ' ',
		else:	
			print 'x',

	print		
