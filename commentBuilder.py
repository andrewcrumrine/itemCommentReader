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
		self.header = ['Item Name','NS ID','Comment 1','Comment 2','Comment 3',\
			'Comment 4', 'Comment 5', 'Comment 6', 'Comment 7', 'Comment 8',\
			'Comment 9', 'Comment 10', 'Comment 11', 'Comment 12', 'Comment 13',\
			'Comment 14', 'Comment 15', 'Comment 16', 'Comment 17', 'Comment 18',\
			'Comment 19', 'Comment 20']
		self.indices = {'Item Name':[0,17],'Com 1':[17,72], 'Com 2':[72,127]}
		self.orderedInd = ['Item Name','Com 1','Com 2']
		self.itemMap = {}
		self.fileOut = filenameIn
		self._createCSV()
		self._createHeader()
		self._setItemMap('itemMap.txt')
		self.item = None

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

	def _getNSID(self):
		"""
	Return the NS ID after checking the item Map
		"""
		return self.itemMap[self.item]


	def writeToCSV(self,textIn,index,length):
		"""
	Specific writeToCSV for comment builder
		"""
		self._setText(textIn)
		self.item = self._getItem()
		if self._isItemInMap(self.item):
			self._setCommentEntry(index,length)

	def _setCommentEntry(self,index,length):
		"""
	This method manages the data writen to the csv file.  It saves the
	comment data to be used on other entries.
		"""

		for ind in self.orderedInd:
			if index == 0 and ind == 'Item Name':
				self._setAltField(self.item)
				self._nextField()
				self._setAltField(self._getNSID())
				self._nextField()
			elif ind == 'Com 1' or ind == 'Com 2':
				self._setCommentField(ind)
				self._nextField()
		if index == length - 1:
			self._nextEntry()

	def _setCommentField(self,textIn,fid=None):
		"""
	Writes field to csv
		"""
		if fid is None:
			fid = self.fid
		textOut = self.iterText(textIn)
		textOut = s.removeSpaces(textOut)
		textOut = s.removeCommas(textOut)
		fid.write(textOut)

	def _setAltField(self,textIn,fid=None):
		"""
	Writes to csv without using iterText.  Overrides the header key.
		"""
		if fid is None:
			fid = self.fid
		fid.write(textIn)

	def _getItem(self):
		"""
	Get item value from incoming text 
		"""
		item = self.iterText('Item Name')
		item = s.removeSpaces(item)
		return item

	def _isItemInMap(self,itemIn):
		"""
	Check if item is in map
		"""
		return self.itemMap.has_key(itemIn)
