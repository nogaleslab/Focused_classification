#!/usr/bin/env python

import optparse
from sys import *
import os,sys,re
from optparse import OptionParser
import glob
import subprocess
from os import system
import linecache

#=========================
def setupParserOptions():
        parser = optparse.OptionParser()
        parser.set_usage("%prog -s <classums stack> -f <merged distances file> --topX=x --topY=y --botX=x --botY=y")
        parser.add_option("-s",dest="stack",type="string",metavar="FILE",
                help="stack of selected, classified averages")
	parser.add_option("-f",dest="dist",type="string",metavar="FILE",
                help="Merged distances file")
	parser.add_option("--topX",dest="topX",type="float", metavar="FLOAT",
		help="top left corner of box to use,x coordinate")
	parser.add_option("--topY",dest="topY",type="float", metavar="FLOAT",
                help="top left corner of box to use,y coordinate")
	parser.add_option("--botX",dest="botX",type="float", metavar="FLOAT",
                help="bottom right corner of box to use, x coordinate")
	parser.add_option("--botY",dest="botY",type="float", metavar="FLOAT",
                help="bottom right corner of box to use, y coordinate")
	parser.add_option("-d", action="store_true",dest="debug",default=False,
                help="debug")
        options,args = parser.parse_args()

        if len(args) > 0:
                parser.error("Unknown commandline options: " +str(args))

        if len(sys.argv) < 2:
                parser.print_help()
		sys.exit()
        params={}
        for i in parser.option_list:
                if isinstance(i.dest,str):
                        params[i.dest] = getattr(options,i.dest)
        return params

#=========================

def compare(params):

	topX = params['topX']
	topY = params['topY']
	botX = params['botX']
	botY = params['botY']

	stack = params['stack']
	f = params['dist']
	o = '%s_sel_%sx_%sy_%sx_%sy.plt' %(f[:-4],str(topX)[:-2],str(topY)[:-2],str(botX)[:-2],str(botY)[:-2])

	if os.path.exists(o):
		os.remove(o)
	dist = open(f,'r')
	out = open(o,'w')

	i=0

	for line in dist:

		l = line.split()
		if line[1] is ';':
                        continue
		AC = float(l[2])
		BC = float(l[3])

		if botX >= AC >= topX and topY >= BC >= botY:

			out.write('%s\n' %(i))

		i = i +1

	out.close()
	return o
	
def makeStack(params,o):

	stack = params['stack']
	topX = params['topX']
        topY = params['topY']
        botX = params['botX']
        botY = params['botY']

	cmd = 'proc2d %s %s_sel_%sx_%sy_%sx_%sy.img list=%s' %(stack,stack[:-4],str(topX)[:-2],str(topY)[:-2],str(botX)[:-2],str(botY)[:-2],o)
	subprocess.Popen(cmd,shell=True).wait()

	cmd = 'proc2d %s_sel_%sx_%sy_%sx_%sy.img %s_sel_%sx_%sy_%sx_%sy_tot.img average' %(stack[:-4],str(topX)[:-2],str(topY)[:-2],str(botX)[:-2],str(botY)[:-2],stack[:-4],str(topX)[:-2],str(topY)[:-2],str(botX)[:-2],str(botY)[:-2])
	subprocess.Popen(cmd,shell=True).wait()

if __name__ == "__main__":

	params=setupParserOptions()
	o = compare(params)
	makeStack(params,o)
