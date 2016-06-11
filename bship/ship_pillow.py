#!/usr/bin/python

from PIL import Image
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -2.2
X_MAX =  2.2
Y_MIN = -1.8
Y_MAX =  1.8
offset =  0.01
maxiter = 80
calc_count = 0
rnum = 31
bnum = 30 
lenlc  =  len( colour_list )

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

#print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
X_SIZE += 1
Y_SIZE += 1

X_SIZE     = int( X_SIZE )
Y_SIZE     = int( Y_SIZE )
white      = (255,255,255)
randcolour = ( 000, 000, 000 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( 0, 0 )
		C = complex ( X, Y )
		#Z = complex ( X, Y )
		iter = 0

		while ( abs ( Z**2 ) < 4 and iter < maxiter ):
			Z = complex( abs( Z.real ) , abs( Z.imag ) )
			Z = Z**2 + C
			iter = iter + 1
			calc_count = calc_count + 1
		#print X, Y , Z, iter
		#mycolour = ( 3 * iter, 2 * iter, 7 * iter )  
		#img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		'''
                if ( iter > 3 and iter <= 30 ):
			mycolour = colour_list[ iter + rnum ]
		else:
			mycolour = colour_list[ iter % lenlc  ]
		if ( iter <= 3 ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 

		elif ( iter == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		'''
		if ( iter == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), white ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

print 'Burning Ship Julia for',C , 'and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count


img.show()

