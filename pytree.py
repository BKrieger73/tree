#!/usr/bin/env python3
import subprocess
import sys
import os

# YOUR CODE GOES here

def printTree(d, depth, fullpath, isLast, pipes) :
	nbsp = ""
	depth = depth + 1	
	#print(fullpath+d)
	chr = "|"
	if isLast :
		chr = "`"
	if (os.path.isdir(fullpath + "/" + d)) :
		if (depth>0) :
			for i in range(depth) :
				try :
					if pipes.index(i) > -1 : 
						nbsp = nbsp + "|   "
				except :
					nbsp = nbsp + "   "
			nbsp = "|" + nbsp		
		print(nbsp + chr + "-- " + d)
		dirs = os.listdir(fullpath + "/" + d)
		if not isLast and depth > 0:
			pipes.append(depth)
		for j in range(len(dirs)) :
			if not (dirs[j].startswith(".")) :				
				printTree(dirs[j], depth, fullpath + "/" + d, ( j == len(dirs) - 1), pipes)
	else :
		#print(pipes)
		for i in range(depth) :
			try :
				if pipes.index(i) > -1 : 
					nbsp = nbsp + "|   "
			except :
				nbsp = nbsp + "   "
		if isLast and len(pipes) > 0 :
			pipes.remove(pipes[len(pipes)-1])
		if (depth>1) :
			nbsp = "|" + nbsp
		print(nbsp + chr + "-- " + d)	


if __name__ == '__main__':
	cwd = os.getcwd()
	dirs = os.listdir(cwd)
	depth = -1
	pipes = []
	print(".")
	for i in range(len(dirs)) : 
		isLast = ( i == len(dirs) - 1)
		if not (dirs[i].startswith(".")) :
			printTree(dirs[i], depth, cwd, isLast, pipes)
	
	#print(os.listdir(os.getcwd())[0]);
	# just for demo
	# subprocess.run(['tree'] + sys.argv[1:])
