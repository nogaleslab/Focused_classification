#!/usr/bin/env python

import glob
import linecache
import math 
import sys
import os

#To run:
#./calc_distance_lobeA_NEWJan2012.py boxed.lis

list = open(sys.argv[1],'r')
c = 1
for f in list:

        c = 1 + c
i = 1

radConv = 180/(math.pi)

o1 = 'distanceA.spi'
o2 = 'distanceB.spi'

out1 = open(o1,'w')
out2 = open(o2,'w')
#out3 = open(o3,'w')

def rotate(x,y,theta):

	theta=(theta*(math.pi))/180
	cos = math.cos(theta)
	sin = math.sin(theta)	
	xt = x*cos - y*sin
	yt= x*sin + y*cos
	
	return xt,yt

while i < c:

	g = linecache.getline(sys.argv[1],i)
        n = '%s.box'%(g[:-5])

	tmp = '%s' %(n[5:])
        selClass = '%s' %(tmp[:-4])

	test = os.path.exists(n)
	if test is False:
		i = i + 1
		continue
	l0 = linecache.getline(n,1)
	l1 = linecache.getline(n,2)
	l2 = linecache.getline(n,3)

	j0 = l0.split()
	j1 = l1.split()
	j2 = l2.split()

	x0=float(j0[0])-float(j0[0])
	y0=float(j0[1])-float(j0[1])

	x1=float(j1[0])-float(j0[0])
	y1=float(j1[1])-float(j0[1])

	x2=float(j2[0])-float(j0[0])
	y2=float(j2[1])-float(j0[1])
	
	line01 = math.sqrt((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1))

	if x0 < x1:

		#xprime = (((-y1)*(x1-x0))/(y1-y0)) + x1

		S = math.fabs(x1) 
	
		alpha =  math.atan(y1/S)*radConv
	if x0 > x1:

		#print 'x0 > x1'
		#xprime = (((-y1)*(x1-x0))/(y1-y0)) + x1

		S = math.fabs(x1)  
	
		alpha = 180 + (math.atan(math.fabs(y1)/S)*radConv)
	#To rotate clockwise, negative angle

	xT1,yT1 = rotate(x1,y1,-alpha)
	xT2,yT2 = rotate(x2,y2,-alpha)

	print "Old coordinates:  x0=%s, y0=%s; x1=%s, y1%s; x2=%s, y2=%s" %(x0,y0,x1,y1,x2,y2)
	print "Rotated coords:   x0=%s, y0=%s; xT1=%s, yT1=%s; xT2=%s, yT2=%s" %(x0,y0,xT1,yT1,xT2,yT2)
	
	n = xT2/xT1

#	M = math.sqrt((xT2-xT1)*(xT2-xT1) + (yT2-yT1)*(yT2-yT1))

#	gamma = (math.asin(yT2/M)*radConv)	

	out1.write('%s	2	%s	%s\n' %(i,n,selClass))
	out2.write('%s 	1 	%s\n' %(i,line01))
#	out3.write('%s	1	%s\n' %(i,gamma))

	i=i+1
