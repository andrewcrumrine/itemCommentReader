"""
	commentBuilder.py

	Comment Builder Module
	----------------------

	This module manages the input of comments read from the file reader.

"""

import fileReader as f
import csvCreator as csv

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
