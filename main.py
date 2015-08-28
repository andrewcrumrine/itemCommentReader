#! /usr/bin/python

"""
	main.py

	Main File in Item Comment Reading Program
	-----------------------------------------

"""

import fileReader as f
import manageFiles as m

HEADER_KEY_START = 'Item       '
HEADER_KEY_STOP = 'Number\n'

PATH = 'ItemBuildInstructions'


def main():
	files = m.FileList(PATH)
	print files.files

	x = []

	while not files.isEmpty():
		out = []
		inFile = f.TxtFileReader(files.getNextFile(),HEADER_KEY_START,HEADER_KEY_STOP)

		while inFile.reading:
			lineOut = inFile.getNextLine()
			if lineOut is not None:
				out.append(lineOut.getText())
		x.append(out)
	return x

if __name__ == "__main__":
	main()
