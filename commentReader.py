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
		HEAD_START = 'Item'
		HEAD_STOP = 'Number\n'
		self.headerKey = ['Item','Number\n']
		f.TxtFileReader.__init__(self,filenameIn)

	def __del__(self):
		"""
	Closes the open file stream
		"""
		f.TxtFileReader.__del__(self)

class CommentBuffer(f.TxtBuffer):
	"""
	This class extends the TxtBuffer class.  Used to read comment
	files and remove unwanted lines.
	"""
	def __init__(self,fid,beginning,key):
		"""
	Initializes the Comment Buffer class.  Sometimes the special line
	needs to be searched at the beginning, sometimes at the end.  It
	will always need a key.
		"""
		f.TxtBuffer.__init__(self,fid,beginning,key)