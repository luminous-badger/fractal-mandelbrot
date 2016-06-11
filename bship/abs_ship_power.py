#!/usr/bin/python

# Ship for powers > 2.
# Real or Imag part to be abs value.
# JM Sat 12 Mar 2016 16:05:06 GMT

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN      = -2.2
X_MAX      =  2.2
Y_MIN      = -1.8
Y_MAX      =  1.8
offset     =  0.01
maxiter    = 80
calc_count = 0
rnum       = 31
bnum       = 30 
lenlc      = len( colour_list )
ZPower     = 6.0

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

#print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
X_SIZE += 1
Y_SIZE += 1

X_SIZE     = int( X_SIZE )
Y_SIZE     = int( Y_SIZE )
white      = (255,255,255)
randcolour = ( 255, 255, 255 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( 0, 0 )
		C = complex ( X, Y )
		#Z = complex ( X, Y )
		iter = 0

		while ( abs ( Z**ZPower ) < 4 and iter < maxiter ):
			Z = complex( Z.real , abs( Z.imag ) )
			Z = Z**ZPower + C
			iter = iter + 1
			calc_count = calc_count + 1
		#print X, Y , Z, iter
		mycolour = ( 13 * iter, 23 * iter, 33 * iter )  
		#img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		'''
                if ( iter > 3 and iter <= 30 ):
			mycolour = colour_list[ iter + rnum ]
		else:
			mycolour = colour_list[ iter % lenlc  ]
		'''
		if ( iter <= 2 ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 

		elif ( iter == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Burning Ship abs Imag for Z^' + str ( ZPower ) 

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print 'Burning Ship abs Imag for Z^', ZPower, 'and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count


img.show()

