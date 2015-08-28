#! /usr/bin/python

"""
	main.py

	Main File in Item Comment Reading Program
	-----------------------------------------

"""

import fileReader as f

HEADER_KEY_START = 'Item       '
HEADER_KEY_STOP = 'Comments 20\n'

filename = 'ItemBuildInstructions.txt'

buff = f.TxtFileReader(filename,HEADER_KEY_START,HEADER_KEY_STOP)

out = []

while buff.reading:
	line = buff.getNextLine()
	if line is not None:
		out.append(line.getText())

print out