#!/usr/bin/python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -2.0
X_MAX =  2.0
Y_MIN = -1.5
Y_MAX =  1.5
offset =  0.01
maxiter = 80
calc_count = 0
rnum = 31
bnum = 30 
#C = complex ( -0.721, -0.6721 )
#C = complex (  0.3878, -0.0975 )
#C = complex ( -0.615, 0.365 )
#C = complex (  0.265,  0.526 ) 
C = complex ( -1.734, -0.1 ) 
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

def crjulia():	
	C          = complex ( real_part, imag_part )  
	MsgText = 'Julia for ' + str( C ) 
	print MsgText  
	calc_count = 0
	x_pixel = 0
	for X in nm.arange ( X_MIN, X_MAX, offset ):
		y_pixel = 0
		for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
			#Z = complex ( 0, 0 )
			Z = complex ( X, Y )
			iter = 0

			while ( abs ( Z**2 ) < 4 and iter < maxiter ):
				Z = complex( abs( Z.real ) , abs( Z.imag ) )
				#C = complex( abs( C.real ) , abs( C.imag ) )
				Z = Z**2 + C
				iter = iter + 1
				calc_count = calc_count + 1
			#print X, Y , Z, iter
			mycolour = ( 13 * iter, 23 * iter, 23 * iter )  
			'''
			if ( iter > 3 and iter <= 30 ):
				mycolour = colour_list[ iter + 76 ]
			else:
				mycolour = colour_list[ iter % lenlc  ]
			'''
			if ( iter <= 3 ):
				img.putpixel( ( x_pixel,  y_pixel ), white ) 

			elif ( iter == maxiter ):
				img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
			else:
				img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
			y_pixel += 1
		x_pixel += 1

	print 'Calc: ', calc_count
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )

	draw.text( ( 0, 0 ),  MsgText, ( 0,0,0 ), font=font )
	img.show()

'''
End crjulia. 
'''

# for imag_part > 0.8, just get a blank. No Julia ???
# 0.3 to 0.7, ring like, but not much detail.
# 0.3 ok, -1.0 to +0.2, just get rings.
# -1.5 to -1.1 nice pics.
Im_MIN = -1.5
Im_MAX = -0.9
Re_MIN = -0.9
Re_MAX =  0.0
Im_OFF =  0.1
real_part  =  0.0
imag_part  = -1.1
#for imag_part in nm.arange( Im_MIN, Im_MAX, Im_OFF ): 
for real_part in nm.arange( Re_MIN, Re_MAX, Im_OFF ): 
	print 'Real:', real_part, 'Imag:', imag_part
	crjulia()
