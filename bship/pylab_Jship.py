#!/usr/bin/python

from pylab import imshow, show
import numpy as nm
import cmath
from timeit import default_timer as timer

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
#C = complex ( -0.721, -0.6721 )
#C = complex (  0.3878, -0.0975 )
C = complex (  0.5878, -0.0875 )
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

image = nm.zeros(( Y_SIZE, X_SIZE ), dtype = nm.uint8)

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		#Z = complex ( 0, 0 )
		#C = complex ( X, Y )
		Z = complex ( X, Y )
		iter = 0
		y_pixel += 1

		while ( abs ( Z**2 ) < 4 and iter < maxiter ):
			Z = complex( abs( Z.real ) , abs( Z.imag ) )
			Z = Z**2 + C
			iter = iter + 1
			calc_count = calc_count + 1
		#print X, Y , Z, iter
		image[ y_pixel, x_pixel ] = iter + rnum
	x_pixel += 1

dt = timer() - start

print 'Burning Ship Julia for',C , 'and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count

imshow(image)
show()

