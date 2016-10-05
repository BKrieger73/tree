#!/usr/bin/env python3
import subprocess
import sys
import os


def printTree(d, depth, fullpath, isLast, pipes, directories, files) :
	nbsp = ""
	depth = depth + 1	
	chr = "├──"
	if isLast :
		chr = "└──"
	if (os.path.isdir(fullpath + "/" + d)) :
		directories = directories + 1
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
		if (not isLast ) : 
			pipes.append(depth)
		for j in range(len(dirs)) :
			if not (dirs[j].startswith(".")) :				
				directories, files = printTree(dirs[j], depth, fullpath + "/" + d, ( j == len(dirs) - 1), pipes, directories, files)
	else :
		files = files + 1;
		for i in range(depth) :
			try :
				if pipes.index(i) > -1 : 
					nbsp = nbsp + "│    "
			except :
				nbsp = nbsp + "    "			
		if isLast and len(pipes) > 0 :
			pipes.remove(pipes[len(pipes)-1])
		print(nbsp + chr + " " + d)	
	return directories, files


if __name__ == '__main__':
	directories = 0;
	files = 0;
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
			directories, files = printTree(dirs[i], depth, cwd, isLast, pipes, directories, files)
	print()
	print(str(directories) + " directories,  " + str(files) + " files")