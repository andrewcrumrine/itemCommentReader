"""
	commentBuilder.py

	Comment Builder Module
	----------------------

	This module manages the input of comments read from the file reader.

"""

class CSVCreator(object):
	"""
	CSVCreator on the Comment Builder Module builds a csv with every comment
	fields inputed from the AS400
	"""

	def __init__(self,filenameIn):
		"""
	This initializes the CSVCreator object.
		"""
		self.fileIn = filenameIn
		self.fileOut = 'out.csv'
		self.text = ''
		self.fid = None
		self.csvCreated = False

		self.itemMap = {}
		self.header = []
		self.indices = {}

		self.header = ['Item Name','Comment 1','Comment 2','Comment 3',\
			'Comment 4', 'Comment 5', 'Comment 6', 'Comment 7', 'Comment 8',\
			'Comment 9', 'Comment 10', 'Comment 11', 'Comment 12', 'Comment 13',\
			'Comment 14', 'Comment 15', 'Comment 16', 'Comment 17', 'Comment 18',\
			'Comment 19', 'Comment 20']

		self.indices = {'Item Name':[0,17],'Com 1':[17,72], 'Com 2':[72,127]}
		if type(self) == CSVCreator:
			self._createCSV()

	def __del__(self):
		"""
	This method runs when the object is destroyed.  It closes the file.
		"""
		if self.fid is not None:
			self.fid.close()


	def _createCSV(self):
		"""
	Creates the csv output file
		"""
		if self.csvCreated == False:
			self.fid = open(self.fileOut,'w')
			self._createHeader()
			self.csvCreated = True


	def _createHeader(self,fid=None):
		"""
	This method creates the header based off of the previously defined fields.
		"""

		for ind, field in enumerate(self.header):
			self._setField(field)
			if ind != len(self.header) - 1:
				self._nextField(fid)
		self._nextEntry(fid)


	def _nextField(self,fid = None):
		"""
	This method appends a comma to the file output.  Thus dividing two fields.
		"""
		if fid is None:
			fid = self.fid
		fid.write(',')


	def _nextEntry(self,fid = None):
		"""
	This method appends a new line to the file output.  Thus dividing two entires.
		"""
		if fid is None:
			fid = self.fid
		fid.write('\n')

	def _setField(self,field,fid = None):
		"""
	This method writes the input text to the file output.
		"""
		if fid is None:
			fid = self.fid
		fid.write(field)


	def iterText(self,keyIn,textIn=None):
		"""
	This uses the indices ivar to output a splice of the text stream.
		"""
		key1 = self.indices[keyIn][0]
		key2 = self.indices[keyIn][1]
		if textIn is None:
			return self.text[key1:key1]
		else:
			return textIn[key1:key2]

class CommentCreator()