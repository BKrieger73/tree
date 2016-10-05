#!/usr/bin/env python3
import subprocess
import sys
import os

# YOUR CODE GOES here

def printTree(d, depth) :
	nbsp = ""
	depth = depth + 1
	if (os.path.isdir(d) == False) :
		for i in range(depth) :
			nbsp = nbsp + "    "
		print("|" + nbsp + d)
	else :
		print("| -- " + d)
		dirs = os.listdir(d)
		for j in dirs :
			printTree(j, dept

if __name__ == '__main__':
	dirs = os.listdir(os.getcwd())
	depth = -1
	for i in dirs: 
		printTree(i, depth)
	
	#print(os.listdir(os.getcwd())[0]);
	# just for demo
	# subprocess.run(['tree'] + sys.argv[1:])
