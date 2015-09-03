"""
	commentReader.py

	Comment Reader Module
	---------------------

	This module extends classes in the File Reader module.  Used
	to read the comment files used as building instructions to make
	custom items.

"""

import fileReader as f

class CommentFileReader(f.TxtFileReader):
	"""
	This class extends the TxtFileReader.  Used to read the comment
	files.
	"""
	def __init__(self,filenameIn):
		"""
	This initializes the class.  It only takes in the filename
	and passes it to the parent class along with fixed keys.
		"""
		self.headerKey = {'Item':True, 'Number\n':False}
		f.TxtFileReader.__init__(self,filenameIn)

	def __del__(self):
		"""
	Closes the open file stream
		"""
		f.TxtFileReader.__del__(self)

	def getNextLine(self):
		"""
	This method creates a CommentBuffer object.  It tells the
	program when there are no more lines to read.
		"""

		self.buffer = CommentBuffer(self.fid,self.headerKey)
		self._setReading()
		if self._isReturnLine():
			return self.buffer
		else:
			return None

class CommentBuffer(f.TxtBuffer):
	"""
	This class extends the TxtBuffer class.  Used to read comment
	files and remove unwanted lines.
	"""
	def __init__(self,fid,keys):
		"""
	Initializes the Comment Buffer class.  Sometimes the special line
	needs to be searched at the beginning, sometimes at the end.  It
	will always need a key.
		"""
		f.TxtBuffer.__init__(self,fid)
		self.keys = keys
		self.returnLine = self._checkAllReturnLines()


	def _checkAllReturnLines(self):
		"""
	Check all return line conditions
		"""
		for key, direction in self.keys.iteritems():
			self._setKey(key)
			self._setPosition(direction)
			if not self._checkReturnLine():
				return False
		return True