class Document:
	def __init__(self, docID):
		self.docID = docID
		self.word_freq = 0
		self.title = 0
		self.h = 0
		self.body = 0
		self.strong = 0

	def __repr__(self):
		output = "[DocID: %s, freq: %d, title: %d, h: %d, body: %d, strong: %d]" % (self.docID, self.word_freq, self.title, self.h, self.body, self.strong)
		return output