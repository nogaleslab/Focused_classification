#!/usr/bin/env python

import optparse
from sys import *
import os,sys,re
from optparse import OptionParser
import subprocess
from os import system
import linecache

#=========================
def setupParserOptions():
        parser = optparse.OptionParser()
        parser.set_usage("%prog -p <plt file> -s <classums_stack> -b <boxed.lis file> ")
        parser.add_option("-p",dest="plt",type="string",metavar="FILE",
                help="PLT output file from msa classums header")
	parser.add_option("-s",dest="stack",type="string",metavar="FILE",
                help="msa classums stack")
        parser.add_option("-b",dest="boxed",type="string",metavar="FILE",
                help="List of box files (ls *.box > boxed.lis)")
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

def select(params):

	plt = params['plt']
        stack = params['stack']
        boxed = params['boxed']

	f = open(boxed,'r')
	out = '%s_sel.plt' %(plt[:-4])
	if os.path.exists(out):
		os.remove(out)

	if os.path.exists('%s_sel.img' %(stack[:-4])):
		os.remove('%s_sel.img' %(stack[:-4]))
		os.remove('%s_sel.hed' %(stack[:-4]))
	out2 = '%s_selPartList.plt' %(stack[:-4])
	if os.path.exists(out2):
		os.remove(out2)	
	o1 = open(out,'w')
	o2 = open(out2,'w')

	for line in f:

		newLine = '%s' %(line[:-5])
		
		newLine2 = '%s' %(newLine[5:])
		
		selMSA = linecache.getline(plt,int(newLine2))
		o1.write(selMSA)
		emanNum = float(newLine2) - 1
		o2.write('%s\n' %(str(emanNum)[:-2]))

	o1.close()
	f.close()

	#cmd = '/home/michael/BATCHLIB/ex_co.b %s %s' %(stack,out2)
	#print cmd 
	#subprocess.Popen(cmd,shell=True).wait()

	cmd = "proc2d %s %s_sel.img list=%s" %(stack,stack[:-4],out2)
	print 'Run this command:\n'
	print '\n'
	print '		%s\n' %(cmd)
	print '\n' 
	#subprocess.Popen(cmd,shell=True).wait()

	#emancmd = "proc2d %s %s_sel.img list=%s" %(stack,stack[:-4],out2)
        #print emancmd
	#p = subprocess.Popen(emancmd, shell=True, stdout=subprocess.PIPE)
        #p.wait()

if __name__ == "__main__":

	params=setupParserOptions()
	select(params)
