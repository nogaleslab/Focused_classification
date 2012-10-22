#!/usr/bin/env python

import linecache
import math 
import sys
import os

#To run:
#./calc_distance_A_to_C.py boxed.lis

def distA_C(box_list,numFiles,o1):

	i = 1

	output = open(o1,'w')
	
	while i <= numFiles:

		boxFile = linecache.getline(box_list,i)
		
		boxFile = boxFile[:-1] 	

		test = os.path.exists(boxFile)

		if test is False:
			print "%s file doesn't exist - do something." %(boxFile)
			sys.exit()
		
		A = linecache.getline(boxFile,1)
		B = linecache.getline(boxFile,2)
		C = linecache.getline(boxFile,3)

		A0 = A.split()
		B0 = B.split()
		C0 = C.split()

		distanceAC = math.sqrt(((float(A0[0]) - float(C0[0]))*(float(A0[0]) - float(C0[0]))) + ((float(A0[1]) - float(C0[1]))*(float(A0[1]) - float(C0[1]))))

		output.write('%s	1	%f\n' %(str(i),distanceAC))

		i = i + 1

if __name__ == "__main__":

	box_list = sys.argv[1]	
	box_open = open(box_list,'r')
	numFiles = len(box_open.readlines())

	#Output
	o1 = 'distanceA_C.spi'

	testOut = os.path.exists(o1)

	if testOut is True:
		print '%s file exists - remove file then re-run script' %(o1)
		sys.exit()
	
	distA_C(box_list,numFiles,o1)
	
