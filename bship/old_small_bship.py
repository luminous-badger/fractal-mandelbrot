#!/usr/bin/python

from pylab import imshow, show
import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -2.5
X_MAX =  1.5
Y_MIN = -2.0
Y_MAX =  1.0

X_MIN =  0.2
X_MAX =  1.3
Y_MIN = -2.0
Y_MAX = -0.5
offset =  0.001
maxiter = 80
calc_count = 0
rnum = 3
bnum = 70 
mnum = 99 

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

#print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
X_SIZE += 1
Y_SIZE += 1

image = nm.zeros(( Y_SIZE, X_SIZE ), dtype = nm.uint8)

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( 0, 0 )
		C = complex ( X, Y )
		iter = 0
		y_pixel += 1

		while ( abs ( Z**2 ) < 4 and iter < maxiter ):
			Z = complex( abs( Z.real ) , abs( Z.imag ) )
			Z = Z**2 + C
			iter = iter + 1
			calc_count = calc_count + 1
			#print X, Y , Z
		if ( iter <= 10 ):	
			image[ y_pixel, x_pixel ] = bnum
		elif ( iter == maxiter ):	
			image[ y_pixel, x_pixel ] = mnum
		else:	
			image[ y_pixel, x_pixel ] = iter * rnum
		#image[ y_pixel, x_pixel ] = iter
	x_pixel += 1

dt = timer() - start

print 'Burning Ship and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count

imshow(image)
show()

