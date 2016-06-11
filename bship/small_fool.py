#!/usr/bin/python

# Ship Julia for April Fool's day. Close up of top corner.

from PIL import Image
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -0.4
X_MAX =  0.4
Y_MIN = -1.0
Y_MAX = -0.1
offset =  0.001
maxiter = 80
calc_count = 0
rnum = 31
bnum = 30 
#C = complex ( -0.721, -0.6721 )
#C = complex (  0.3878, -0.0975 )
C = complex (  -0.41, 0.14 )
lenlc  =  len( colour_list )
"""
Wikipedia mentions 'corresponding Julia fractal' so set value of C here.
Using -0.683, 0.383 generates a solid block of colour ...
Ooops ... forgot tp set Z = x + iy in the loop.
C = complex ( 0.56667, -0.5 ) - not bad.
C = complex ( -1.734, -0.1 ) nice ...
From: http://coloryourfractals.com/fractals/burningship-julia.php
"""

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

#print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
X_SIZE += 1
Y_SIZE += 1

X_SIZE     = int( X_SIZE )
Y_SIZE     = int( Y_SIZE )
white      = (255,255,255)
randcolour = ( 190, 190, 190 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		#Z = complex ( 0, 0 )
		Z = complex ( X, Y )
		iter = 0

		while ( abs ( Z**2 ) < 4 and iter < maxiter ):
			Z = complex( abs( Z.real ) , abs( Z.imag ) )
			Z = Z**2 + C
			iter = iter + 1
			calc_count = calc_count + 1
		#print X, Y , Z, iter
		#mycolour = ( 1 * iter, 1 * iter, 1 * iter )  
                if ( iter > 3 and iter <= 30 ):
			mycolour = colour_list[ iter + 56 ]
		else:
			mycolour = colour_list[ iter + 41  ]
			#mycolour = colour_list[ iter % lenlc  ]
		if ( iter <= 3 ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 

		elif ( iter == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1
	x_pixel += 1

dt = timer() - start

print 'Burning Ship Julia for',C , 'and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count


#img.show()
img.save( 'AprilFoolSmall.png' )
