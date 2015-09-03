#! /usr/bin/python

"""
	main.py

	Main File in Item Comment Reading Program
	-----------------------------------------

"""

import commentReader as cR
import manageFiles as m
import commentBuilder as cB

HEADER_KEY_START = 'Item       '
HEADER_KEY_STOP = 'Number\n'

PATH = 'ItemBuildInstructions'
fileOut = 'itemComments.csv'


def main():
	csvOut = cB.CommentCreator(fileOut)
	files = m.FileList(PATH)
	print(files.files)
	openfiles = []


	while not files.isEmpty():
		openfiles.append(cR.CommentFileReader(files.getNextFile(False)))

	while openfiles[-1].reading:
		for reader in openfiles:
			lineOut = reader.getNextLine()
			if lineOut is not None:
				csvOut.writeToCSV(lineOut.getText(1),openfiles.index(reader),len(openfiles))
				pass

if __name__ == "__main__":
	main()
