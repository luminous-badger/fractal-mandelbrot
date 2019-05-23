#!/usr/bin/python3

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Julias for Z^ZPower.
# Args from command line.
# JM Fri 25 Jan 16:32:07 GMT 2019

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list
import sys

start = timer()

X_MIN = -3.5
X_MAX =  3.5 
Y_MIN = -3.4
Y_MAX =  3.4
offset     = 0.01
maxiter    = 175
calc_count = 0
rnum       = 94
#rnum       = int( sys.argv[ 1 ] )
ZPower     = 1.7 
CReal      = float( sys.argv[ 1 ] )
CImag      = float( sys.argv[ 2 ] )
C          = complex ( CReal, CImag )

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print ( 'X: ', X_SIZE ,' Y: ', Y_SIZE  )

white      = (255,255,255)
randcolour = (255,218,255)
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
lenlc      =  len( colour_list ) 

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0
		#print 'XYZ:', X,Y,Z

		while ( abs ( Z**ZPower ) < 4 and iter_count < maxiter ):
			Z = Z**ZPower + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		if ( iter_count + rnum  >= lenlc ):
			mycolour = colour_list[ iter_count % lenlc ]
		else:
			mycolour = colour_list[ iter_count + rnum  ]
		if ( iter_count <= 2 ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 
		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Julia for Z^' + str( ZPower ) + ' ' + str( C ) + ' Rnum: ' + str( rnum ) 

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-B.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 0,0,0 ), font=font )

#print 'Julia for:', C, 'created in %f s' % dt
print ( MsgText , 'created in %f s' % dt )
print  ( 'X: ' + str( X_MAX ) + ' ' + str( X_MIN ) + ' Y: ' + str( Y_MAX ) + ' ' + str( Y_MIN )  )
print ( 'Calc: ', calc_count )

fname = 'Julia_Z' + str( ZPower ) + '_' + str( C.real ) + '_' + str( C.imag )+ '_' + '.png'
print ( 'Fname:', fname )

#img.show()
img.save( fname )

