#!/usr/bin/env python

#To run:
#./make_list_avgsInBin.py [distance.spi file] [lower limit (fraction)] [upper limit (fraction)] [stack].img

import sys
import subprocess

low2 = float(sys.argv[2])
high2 =float(sys.argv[3])
stack = sys.argv[4]
f = sys.argv[1]
o = '%s_selA_C_%02f_%02f.plt' %(f[:-4],low2,high2)

file = open(f,'r')
out = open(o,'w')

i=0

for line in file:

	l = line.split()
	q = float(l[2])

	if q >= low2 and q <= high2:

		out.write('%s\n' %(i))

	i = i +1

out.close()

cmd = 'proc2d %s %s_%02f_%02f.img list=%s' %(stack,stack[:-4],low2,high2,o)
subprocess.Popen(cmd,shell=True).wait()

cmd = 'proc2d %s_%02f_%02f.img %s_%02f_%02f_tot.img average' %(stack[:-4],low2,high2,stack[:-4],low2,high2)
subprocess.Popen(cmd,shell=True).wait()

