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
		f.TxtFileReader.__init__(self,filenameIn,HEAD_START,HEAD_STOP)

	def __del__(self):
		"""
	Closes the open file stream
		"""
		f.TxtFileReader.__del__(self)