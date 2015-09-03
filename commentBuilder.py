"""
	commentBuilder.py

	Comment Builder Module
	----------------------

	This module manages the input of comments read from the file reader.

"""

import fileReader as f
import csvCreator as csv
import stringMan as s

class CommentCreator(csv.CSVCreator):
	"""
	Extends on the CSV Creator object for the comments project
	"""
	def __init__(self,filenameIn):
		"""
	Initializes the comment creator object
		"""
		csv.CSVCreator.__init__(self,filenameIn)
		self.header = ['Item Name','Comment 1','Comment 2','Comment 3',\
			'Comment 4', 'Comment 5', 'Comment 6', 'Comment 7', 'Comment 8',\
			'Comment 9', 'Comment 10', 'Comment 11', 'Comment 12', 'Comment 13',\
			'Comment 14', 'Comment 15', 'Comment 16', 'Comment 17', 'Comment 18',\
			'Comment 19', 'Comment 20']
		self.indices = {'Item Name':[0,17],'Com 1':[17,72], 'Com 2':[72,127]}
		self.itemMap = {}
		self.fileOut = filenameIn
		self._createCSV()
		self._createHeader()

	def __del__(self):
		"""
	Deletes the comment creator object
		"""
		csv.CSVCreator.__del__(self)

	def _setItemMap(self,fileIn):
		"""
	Set the item map ivar using the MapReader function
		"""
		self.itemMap = f.MapReader(fileIn).getMap()


	def writeToCSV(self,textIn,index):
		"""
	Specific writeToCSV for comment builder
		"""
		self._setText(textIn)
		#self._setCommentEntry(index)
		self.testEntry()

	def _setCommentEntry(self,index):
		"""
	This method manages the data writen to the csv file.  It saves the
	comment data to be used on other entries.
		"""
		for ind,rng in self.indices.iteritems():
			if index == 0 and ind == 'Item Name':
				self._setCommentField(ind)
				self._nextField()
			elif ind == 'Com 1' or ind == 'Com 2':
				self._setCommentField(ind)
				self._nextField()
		if index == 9:
			self._nextEntry()

	def testEntry(self):
		self._setCommentField('Com1')

	def _setCommentField(self,textIn,fid=None):
		"""
	Writes field to csv
		"""
		if fid is None:
			fid = self.fid
		textOut = self.iterText(textIn)
		textOut = s.removeSpaces(textOut)
		fid.write(textOut)
