#! /usr/bin/python

"""
	main.py

	Main File in Item Comment Reading Program
	-----------------------------------------

"""

import commentReader as cR
import manageFiles as m

HEADER_KEY_START = 'Item       '
HEADER_KEY_STOP = 'Number\n'

PATH = 'ItemBuildInstructions'


def main():
	files = m.FileList(PATH)
	print(files.files)

	x = []
	y = []
	while not files.isEmpty():
		x.append(cR.CommentFileReader(files.getNextFile(False)))

	while x[-1].reading:
		out = []
		for reader in x:
			lineOut = reader.getNextLine()
			if lineOut is not None:
				out.append(lineOut.getText())
		y.append(out)
	return y

if __name__ == "__main__":
	main()
