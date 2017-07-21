#!/usr/bin/python

# PYLAB version with save. Prints GRID on picture.
# Save the figure before you show() by calling plt.gcf() for "get current figure", then
# you can call savefig() on this Figure object at any time.
# From: https://stackoverflow.com/questions/9012487/matplotlib-pyplot-savefig-outputs-blank-image
# Was saving grid only, or just a blank screen.
# Adding the gcf fixed that problem.


#from pylab import imshow, show, savefig, gcf
import pylab as plt
import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -2.0
X_MAX =  0.8
Y_MIN = -1.2
Y_MAX =  1.2
offset     =  0.01
maxiter    = 50
calc_count = 0
rnum       = 3

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

		while ( abs ( Z**2 ) < 4 and iter < maxiter ):
			Z = Z**2 + C
			iter = iter + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		image[ y_pixel, x_pixel ] = iter

		y_pixel += 1

	x_pixel += 1

dt = timer() - start

print 'Mandelbrot and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
fname = 'Pylab_MBrot_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '.png'
print 'Fname:', fname

plt.xlabel( 'Real' )
plt.ylabel( 'Imaginary' )
plt.title( 'Mandelbrot Set' )
plt.grid(True)

fig = plt.gcf()

plt.imshow(image, extent = [ X_MIN, X_MAX, Y_MIN, Y_MAX ] )
plt.show()
#fig.savefig( 'pylb2.png' )
#fig.savefig( fname )
