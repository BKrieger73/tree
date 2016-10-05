#!/usr/bin/env python3
import subprocess
import sys
import os

def printTree(d, depth, fullpath, isLast, pipes) :
	nbsp = ""
	depth = depth + 1	
	chr = "├──"
	if isLast :
		chr = "└──"
	if (os.path.isdir(fullpath + "/" + d)) :
		if (depth>0) :
			for i in range(depth) :
				try :
					if pipes.index(i) > -1 : 
						nbsp = nbsp + "│    "
				except :
					nbsp = nbsp + "    "	
		print(nbsp + chr + " " + d)
		dirs = os.listdir(fullpath + "/" + d)
		dirs.sort()
		if not isLast and depth > 0:
			pipes.append(depth)
		for j in range(len(dirs)) :
			if not (dirs[j].startswith(".")) :				
				printTree(dirs[j], depth, fullpath + "/" + d, ( j == len(dirs) - 1), pipes)
	else :
		for i in range(depth) :
			try :
				if pipes.index(i) > -1 : 
					nbsp = nbsp + "│    "
			except :
				nbsp = nbsp + "    "
		if isLast and len(pipes) > 0 :
			pipes.remove(pipes[len(pipes)-1])
		print(nbsp + chr + " " + d)	


if __name__ == '__main__':
	if len(sys.argv) == 2 :
		print(sys.argv[1])
		cwd = sys.argv[1]
	elif len(sys.argv) == 1 :
		print(".")
		cwd = os.getcwd()
	else :
		print("incorrect number of arguments")
		exit()
	dirs = os.listdir(cwd)
	depth = -1
	pipes = []
	dirs.sort()
	for i in range(len(dirs)) : 
		isLast = ( i == len(dirs) - 1)
		if not (dirs[i].startswith(".")) :
			printTree(dirs[i], depth, cwd, isLast, pipes)