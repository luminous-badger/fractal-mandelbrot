#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.

from PIL import Image
import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -2.0
X_MAX =  1.0
Y_MIN = -1.2
Y_MAX =  1.2
offset     = 0.01
maxiter    = 50
calc_count = 0
rnum       = 3

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
randcolour = ( 190, 190, 190 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( 0, 0 )
		C = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = Z**2 + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		mycolour = ( 13 * iter_count, 23 * iter_count, 33 * iter_count ) 
		if ( iter_count <= 3 ):
			try:
				img.putpixel( ( x_pixel,  y_pixel ), white ) 
			except:
				print 'Err: X,Y', x_pixel,  y_pixel
				#pass
		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

print 'Mandelbrot and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
img.show()
#img.save( 'Pillow_brot.png' )

