#!/usr/bin/python

'''
Ship with only one value set to absolute.
Now Julia set with Real abs value.
JM Sat 12 Mar 2016 12:36:54 GMT
'''

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN      = -0.3
X_MAX      =  0.3
Y_MIN      =  0.1
Y_MAX      =  1.1
offset     =  0.001
maxiter    = 80
calc_count = 0
rnum       = 97
bnum       = 30 
lenlc      = len( colour_list )
C          = complex ( -0.217, 0.197 )

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE     = int( X_SIZE )
Y_SIZE     = int( Y_SIZE )
print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
orange                    = (255,165,0)
green              = (0,255,127)
randcolour = ( 200, 055, 255 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		#Z = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = complex( abs( Z.real ) , Z.imag )
			Z = Z**2 + C
			iter_count = iter_count + 1
			calc_count = calc_count + 1
		#print X, Y , Z, iter_count
		#mycolour = ( 13 * iter_count, 23 * iter_count, 33 * iter_count )  
		#img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
	        '''	
		'''	
		if ( iter_count + rnum  >= lenlc ):
			mycolour = colour_list[ iter_count % lenlc ]
		else:   
			mycolour = colour_list[ iter_count + rnum  ]
		
		if ( iter_count <= 3 ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 
		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
	
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Burning Ship Julia with abs Real. C = ' + str( C )

print 'Burning Ship Julia with abs Real, C = ' + str( C ) +  ' and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

#img.show()
img.save( "Ship_Julia_Zoom.png" ) 
